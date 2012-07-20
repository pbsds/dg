..const        = import
..compile      = import
..parse.tree   = import
..parse.syntax = import


else = cond ->
  args1 = parse.tree.matchA: cond parse.syntax.ST_EXPR_IF
  args2 = parse.tree.matchA: cond parse.syntax.ST_EXPR_UNLESS
  parse.syntax.ERROR (not: args1 and not: args2) const.ERR.NOT_AFTER_IF
  args1, args1 or args2


switch = cases ->
  cases = parse.syntax.unwrap: cases
  cases = (cases,) unless cases `isinstance` parse.tree.Closure
  cases = list $ map: q -> (parse.tree.matchA: q parse.syntax.ST_ASSIGN) cases
  parse.syntax.ERROR (not $ all: cases) const.ERR.INVALID_STMT_IN_SWITCH
  cases


compile.r.builtins !! 'else' = (self, cond, otherwise) ->
  '''
    a if b else c
    a unless b else c

    Ternary conditional.

  '''

  is_if, (then, cond) = else: cond
  ptr = self.opcode: 'POP_JUMP_IF_FALSE' cond delta: 0 if     is_if
  ptr = self.opcode: 'POP_JUMP_IF_TRUE'  cond delta: 0 unless is_if
  jmp = self.opcode: 'JUMP_FORWARD'      then delta: 0

  ptr:
  self.load: otherwise
  jmp:


compile.r.builtins !! 'switch' = (self, cases) ->
  '''
    switch $
      condition1 = when_condition1_is_true
      ...
      conditionN = when_conditionN_is_true

    Evaluate the first action assigned to a true condition.
    `if-elif` is probably a better equivalent than `switch-case`.

  '''

  jumps = list $ map: c -> (
    cond, action = c
    next = self.opcode: 'POP_JUMP_IF_FALSE' cond delta: 0
    end  = self.opcode: 'JUMP_FORWARD'    action delta: 0
    next:
    end
  ) $ switch: cases

  self.load: None  # in case nothing matched
  list $ map: x -> (x:) jumps
