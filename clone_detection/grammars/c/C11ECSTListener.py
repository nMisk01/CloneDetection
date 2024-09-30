# Generated from ./clone_detection/grammars/c/C11.g4 by ANTLR 4.13.2
from antlr4 import *
import uuid

from clone_detection.ecst.ecst_tree import ECSTree
from clone_detection.ecst.ecst_node import ECSTNode, ShortToken
from clone_detection.grammars.grammars_registry import LISTENERS


if "." in __name__:
    from .C11Parser import C11Parser
else:
    from C11Parser import C11Parser



# This class defines a complete listener for a parse tree produced by C11Parser.
@LISTENERS.register('c')
class C11ECSTListener(ParseTreeListener):
    def __init__(self):
        self.tree = ECSTree()
        self.current_node = self.tree

    # Enter a parse tree produced by C11Parser#primaryExpression.
    def enterPrimaryExpression(self, ctx:C11Parser.PrimaryExpressionContext):
        act_token = ShortToken('',0,0)
        primary_expression_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'PRIMARY_EXPRESSION')
        self.current_node.add_child(primary_expression_node)
        self.current_node = primary_expression_node

    # Exit a parse tree produced by C11Parser#primaryExpression.
    def exitPrimaryExpression(self, ctx:C11Parser.PrimaryExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#genericSelection.
    def enterGenericSelection(self, ctx:C11Parser.GenericSelectionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        generic_selection_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'GENERIC_SELECTION')
        
        self.current_node.add_child(generic_selection_node)
        self.current_node = generic_selection_node

    # Exit a parse tree produced by C11Parser#genericSelection.
    def exitGenericSelection(self, ctx:C11Parser.GenericSelectionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#genericAssocList.
    def enterGenericAssocList(self, ctx:C11Parser.GenericAssocListContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        generic_assoc_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'GENERIC_ASSOC_LIST')
        
        self.current_node.add_child(generic_assoc_node)
        self.current_node = generic_assoc_node


    # Exit a parse tree produced by C11Parser#genericAssocList.
    def exitGenericAssocList(self, ctx:C11Parser.GenericAssocListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#genericAssociation.
    def enterGenericAssociation(self, ctx:C11Parser.GenericAssociationContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        generic_association_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'GENERIC_ASSOCIATION')
        
        self.current_node.add_child(generic_association_node)
        self.current_node = generic_association_node


    # Exit a parse tree produced by C11Parser#genericAssociation.
    def exitGenericAssociation(self, ctx:C11Parser.GenericAssociationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#postfixExpression.
    def enterPostfixExpression(self, ctx:C11Parser.PostfixExpressionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        postfix_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'POSTFIX_EXPRESSION')
        
        self.current_node.add_child(postfix_node)
        self.current_node = postfix_node


    # Exit a parse tree produced by C11Parser#postfixExpression.
    def exitPostfixExpression(self, ctx:C11Parser.PostfixExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:C11Parser.ArgumentExpressionListContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        argument_expression_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ARGUMENT_EXPRESSION_LIST')
        
        self.current_node.add_child(argument_expression_list_node)
        self.current_node = argument_expression_list_node


    # Exit a parse tree produced by C11Parser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:C11Parser.ArgumentExpressionListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:C11Parser.UnaryExpressionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        unary_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'UNARY_EXPRESSION')
        
        self.current_node.add_child(unary_node)
        self.current_node = unary_node


    # Exit a parse tree produced by C11Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:C11Parser.UnaryExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#unaryOperator.
    def enterUnaryOperator(self, ctx:C11Parser.UnaryOperatorContext):
        token = ctx.getText()
        act_token = ShortToken(token,ctx.start.line,ctx.start.column)
        
        unary_operator_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'UNARY_OPERATOR')
        
        self.current_node.add_child(unary_operator_node)
        self.current_node = unary_operator_node


    # Exit a parse tree produced by C11Parser#unaryOperator.
    def exitUnaryOperator(self, ctx:C11Parser.UnaryOperatorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#castExpression.
    def enterCastExpression(self, ctx:C11Parser.CastExpressionContext):
        token = ctx.getText()
        act_token = ShortToken(token, ctx.start.line, ctx.start.column)
        
        cast_expr_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'CAST_EXPRESSION')
        
        self.current_node.add_child(cast_expr_node)
        self.current_node = cast_expr_node

    # Exit a parse tree produced by C11Parser#castExpression.
    def exitCastExpression(self, ctx:C11Parser.CastExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:C11Parser.MultiplicativeExpressionContext):
        token = ctx.getText()
        act_token = ShortToken(token, ctx.start.line, ctx.start.column)
        
        multiplicative_expr_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'MULTIPLICATIVE_EXPRESSION')
        
        self.current_node.add_child(multiplicative_expr_node)
        self.current_node = multiplicative_expr_node

    # Exit a parse tree produced by C11Parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:C11Parser.MultiplicativeExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:C11Parser.AdditiveExpressionContext):
        token = ctx.getText()
        act_token = ShortToken(token,ctx.start.line,ctx.start.column)
        
        additive_expr_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ADDITIVE_EXPRESSION')
        
        self.current_node.add_child(additive_expr_node)
        self.current_node = additive_expr_node

    # Exit a parse tree produced by C11Parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:C11Parser.AdditiveExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#shiftExpression.
    def enterShiftExpression(self, ctx:C11Parser.ShiftExpressionContext):
        token = ctx.getText()
        act_token = ShortToken(token, ctx.start.line, ctx.start.column)
        
        shift_expr_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'SHIFT_EXPRESSION')
        
        self.current_node.add_child(shift_expr_node)
        self.current_node = shift_expr_node

    # Exit a parse tree produced by C11Parser#shiftExpression.
    def exitShiftExpression(self, ctx:C11Parser.ShiftExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#relationalExpression.
    def enterRelationalExpression(self, ctx:C11Parser.RelationalExpressionContext):
        token = ctx.getText()
        act_token = ShortToken(token, ctx.start.line, ctx.start.column)
        
        relational_expr_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'RELATIONAL_EXPRESSION')
        
        self.current_node.add_child(relational_expr_node)
        self.current_node = relational_expr_node

    # Exit a parse tree produced by C11Parser#relationalExpression.
    def exitRelationalExpression(self, ctx:C11Parser.RelationalExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#equalityExpression.
    def enterEqualityExpression(self, ctx:C11Parser.EqualityExpressionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        equality_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'EQUALITY_OPERATOR')
        
        self.current_node.add_child(equality_node)
        self.current_node = equality_node

    # Exit a parse tree produced by C11Parser#equalityExpression.
    def exitEqualityExpression(self, ctx:C11Parser.EqualityExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#andExpression.
    def enterAndExpression(self, ctx:C11Parser.AndExpressionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        and_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'AND')
        
        self.current_node.add_child(and_node)
        self.current_node = and_node

    # Exit a parse tree produced by C11Parser#andExpression.
    def exitAndExpression(self, ctx:C11Parser.AndExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:C11Parser.ExclusiveOrExpressionContext):
        act_token = ShortToken('^',ctx.start.line,ctx.start.column)
        
        xor_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'XOR')
        
        self.current_node.add_child(xor_node)
        self.current_node = xor_node

    # Exit a parse tree produced by C11Parser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:C11Parser.ExclusiveOrExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:C11Parser.InclusiveOrExpressionContext):
        try:
            act_token = ShortToken(ctx.getText(),ctx.start.line,ctx.start.column)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
        
        inclusive_or_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'BITWISE_OPERATOR')
        
        self.current_node.add_child(inclusive_or_node)
        self.current_node = inclusive_or_node

    # Exit a parse tree produced by C11Parser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:C11Parser.InclusiveOrExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:C11Parser.LogicalAndExpressionContext):
        act_token = ShortToken('&&',ctx.start.line,ctx.start.column)
        
        logical_and_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'LOGICAL_OPERATOR')
        
        self.current_node.add_child(logical_and_node)
        self.current_node = logical_and_node

    # Exit a parse tree produced by C11Parser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:C11Parser.LogicalAndExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:C11Parser.LogicalOrExpressionContext):
        try:
            act_token = ShortToken(ctx.getText(),ctx.start.line,ctx.start.column)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
        
        logical_or_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'LOGICAL_OPERATOR')
        
        self.current_node.add_child(logical_or_node)
        self.current_node = logical_or_node

    # Exit a parse tree produced by C11Parser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:C11Parser.LogicalOrExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#conditionalExpression.
    def enterConditionalExpression(self, ctx:C11Parser.ConditionalExpressionContext):
        try:
            act_token = ShortToken(ctx.getText(),ctx.start.line,ctx.start.column)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
        
        conditional_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'TERNARY')
        
        self.current_node.add_child(conditional_node)
        self.current_node = conditional_node

    # Exit a parse tree produced by C11Parser#conditionalExpression.
    def exitConditionalExpression(self, ctx:C11Parser.ConditionalExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:C11Parser.AssignmentExpressionContext):
        act_token = ShortToken('',0,0)
        assignment_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ASSIGNMENT_EXPRESSION')
        self.current_node.add_child(assignment_node)
        self.current_node = assignment_node

    # Exit a parse tree produced by C11Parser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:C11Parser.AssignmentExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:C11Parser.AssignmentOperatorContext):
        try:
            act_token = ShortToken(ctx.getText(),ctx.start.line,ctx.start.column)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
        
        assignment_operator_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ASSIGNMENT_OPERATOR')
        
        self.current_node.add_child(assignment_operator_node)
        self.current_node = assignment_operator_node

    # Exit a parse tree produced by C11Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:C11Parser.AssignmentOperatorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#expression.
    def enterExpression(self, ctx:C11Parser.ExpressionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        expression_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'EXPRESSION')
        self.current_node.add_child(expression_node)
        self.current_node = expression_node

    # Exit a parse tree produced by C11Parser#expression.
    def exitExpression(self, ctx:C11Parser.ExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#constantExpression.
    def enterConstantExpression(self, ctx:C11Parser.ConstantExpressionContext):
        act_token = ShortToken(ctx.getText(), ctx.start.line, ctx.start.column) 
        constant_node = ECSTNode(
        str(uuid.uuid4()), self.current_node, act_token, 'CONSTANT_EXPRESSION')
        self.current_node.add_child(constant_node) 
        self.current_node = constant_node

    # Exit a parse tree produced by C11Parser#constantExpression.
    def exitConstantExpression(self, ctx:C11Parser.ConstantExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#declaration.
    def enterDeclaration(self, ctx:C11Parser.DeclarationContext):
        act_token = ShortToken('', 0, 0)
        declaration_node = ECSTNode(
        str(uuid.uuid4()), self.current_node, act_token,'DECLARATION')
        self.current_node.add_child(declaration_node)
        self.current_node = declaration_node


    # Exit a parse tree produced by C11Parser#declaration.
    def exitDeclaration(self, ctx:C11Parser.DeclarationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:C11Parser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by C11Parser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:C11Parser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by C11Parser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:C11Parser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by C11Parser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:C11Parser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by C11Parser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:C11Parser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by C11Parser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:C11Parser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by C11Parser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:C11Parser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by C11Parser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:C11Parser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by C11Parser#initDeclarator.
    def enterInitDeclarator(self, ctx:C11Parser.InitDeclaratorContext):
        pass
    #use generic_declaration ???

    # Exit a parse tree produced by C11Parser#initDeclarator.
    def exitInitDeclarator(self, ctx:C11Parser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by C11Parser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:C11Parser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by C11Parser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:C11Parser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by C11Parser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:C11Parser.TypeSpecifierContext):
        act_token = ShortToken('', ctx.start.line, ctx.start.column)
    
        type_specifier = ''
        
        if ctx.INT():
            type_specifier = 'INT'
        elif ctx.CHAR():
            type_specifier = 'CHAR'
        elif ctx.FLOAT():
            type_specifier = 'FLOAT'
        elif ctx.DOUBLE():
            type_specifier = 'DOUBLE'
        elif ctx.VOID():
            type_specifier = 'VOID'
        elif ctx.STRUCT() or ctx.UNION():
            type_specifier = 'STRUCT_OR_UNION'  # ako je neki od ovih tipova
        elif ctx.IDENTIFIER():
            type_specifier = 'USER_TYPE'  # korisnicki tipovi

        type_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            type_specifier
        )
        
        self.current_node.add_child(type_node)
        self.current_node = type_node


    # Exit a parse tree produced by C11Parser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:C11Parser.TypeSpecifierContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:C11Parser.StructOrUnionSpecifierContext):
        token = ctx.getText()
        
        if token.STRUCT():
            act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
            struct_or_union_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'STRUCT')
            self.current_node.add_child(struct_or_union_node)
            self.current_node = struct_or_union_node
        
        elif token.UNION():
            act_token = ShortToken('',ctx.start.line,ctx.start.column)
            
            struct_or_union_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'UNION')
            self.current_node.add_child(struct_or_union_node)
            self.current_node = struct_or_union_node    

    # Exit a parse tree produced by C11Parser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:C11Parser.StructOrUnionSpecifierContext):
        self.current_node = self.current_node.parent



    # Enter a parse tree produced by C11Parser#structOrUnion.
    def enterStructOrUnion(self, ctx:C11Parser.StructOrUnionContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        struct_or_union_type = 'STRUCT' if ctx.STRUCT() else 'UNION'
        
        struct_union_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,struct_or_union_type)
        self.current_node.add_child(struct_or_union_type)
        self.current_node = struct_union_node

    # Exit a parse tree produced by C11Parser#structOrUnion.
    def exitStructOrUnion(self, ctx:C11Parser.StructOrUnionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:C11Parser.StructDeclarationListContext):
        act_token = ShortToken('',0,0)
        struct_declaration_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'STRUCT_DECLARATION_LIST')
        self.current_node.add_child(struct_declaration_list_node)
        self.current_node = struct_declaration_list_node

    # Exit a parse tree produced by C11Parser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:C11Parser.StructDeclarationListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#structDeclaration.
    def enterStructDeclaration(self, ctx:C11Parser.StructDeclarationContext):
        act_token = ShortToken('',0,0)
        struct_declaration_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'STRUCT_DECLARATION')
        self.current_node.add_child(struct_declaration_node)
        self.current_node = struct_declaration_node

    # Exit a parse tree produced by C11Parser#structDeclaration.
    def exitStructDeclaration(self, ctx:C11Parser.StructDeclarationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:C11Parser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by C11Parser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:C11Parser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by C11Parser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:C11Parser.StructDeclaratorListContext):
        act_token = ShortToken('',0,0)
        struct_declarator_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'STRUCT_DECLARATOR_LIST')
        self.current_node.add_child(struct_declarator_list_node)
        self.current_node = struct_declarator_list_node

    # Exit a parse tree produced by C11Parser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:C11Parser.StructDeclaratorListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#structDeclarator.
    def enterStructDeclarator(self, ctx:C11Parser.StructDeclaratorContext):
        act_token = ShortToken('',0,0)
        struct_declarator_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'STRUCT_DECLARATOR')
        self.current_node.add_child(struct_declarator_node)
        self.current_node = struct_declarator_node

    # Exit a parse tree produced by C11Parser#structDeclarator.
    def exitStructDeclarator(self, ctx:C11Parser.StructDeclaratorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:C11Parser.EnumSpecifierContext):
        act_token = ShortToken('',0,0)
        enum_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ENUM_DECL')
        self.current_node.add_child(enum_node)
        self.current_node = enum_node

    # Exit a parse tree produced by C11Parser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:C11Parser.EnumSpecifierContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#enumeratorList.
    def enterEnumeratorList(self, ctx:C11Parser.EnumeratorListContext):
        act_token = ShortToken('', 0,0)
        enumerator_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ENUMERATOR_LIST')
        self.current_node.add_child(enumerator_list_node)
        self.current_node = enumerator_list_node

    # Exit a parse tree produced by C11Parser#enumeratorList.
    def exitEnumeratorList(self, ctx:C11Parser.EnumeratorListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#enumerator.
    def enterEnumerator(self, ctx:C11Parser.EnumeratorContext):
        act_token =ShortToken ('',0,0)
        enumerator_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ENUMERATOR')
        self.current_node.add_child = enumerator_node
        self.current_node = enumerator_node

    # Exit a parse tree produced by C11Parser#enumerator.
    def exitEnumerator(self, ctx:C11Parser.EnumeratorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:C11Parser.EnumerationConstantContext):
        try:
            token = ctx.IDENTIFIER()
            token = token.symbol()
            act_token = ShortToken(token.text,ctx.start.line,ctx.start.column)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
            
        enum_constant_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ENUM_CONSTANT')
        
        self.current_node.add_child(enum_constant_node)
        self.current_node = enum_constant_node

    # Exit a parse tree produced by C11Parser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:C11Parser.EnumerationConstantContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:C11Parser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by C11Parser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:C11Parser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by C11Parser#typeQualifier.
    def enterTypeQualifier(self, ctx:C11Parser.TypeQualifierContext):
        try:
            token = ctx.CONST() or ctx.VOLATILE() or ctx.RESTRICT() 
            if token:
                token = token.symbol
                act_token = ShortToken(token.text, token.line, token.column)
            else:
                act_token = ShortToken('', -1, -1) 
        except AttributeError:
            act_token = ShortToken('', -1, -1) 

        type_qualifier_node = ECSTNode(uuid.uuid4(), self.current_node, act_token,'TYPE_QUALIFIER')
    
        self.current_node.add_child(type_qualifier_node)
        self.current_node = type_qualifier_node 

    # Exit a parse tree produced by C11Parser#typeQualifier.
    def exitTypeQualifier(self, ctx:C11Parser.TypeQualifierContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:C11Parser.FunctionSpecifierContext):
        specifier = ctx.getText() #inline,static,drugi,...
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        function_specifier_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'FUNCTION_SPECIFIER')
        self.current_node.add_child(function_specifier_node)
        self.current_node = function_specifier_node

    # Exit a parse tree produced by C11Parser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:C11Parser.FunctionSpecifierContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:C11Parser.AlignmentSpecifierContext):
        try:
            token = ctx.ALIGNAS() or ctx.INTEGER_CONSTANT()
            if token:
                token = token.symbol()
                act_token = ShortToken(token.text,token.line,token.column)
            else:
                act_token = ShortToken('',-1,-1)
        except AttributeError:
            act_token = ShortToken('',-1,-1)
            
        alignment_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ALIGNMENT_SPECIFIER')
        
        self.current_node.add_child(alignment_node)
        self.current_node = alignment_node
        
        

    # Exit a parse tree produced by C11Parser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:C11Parser.AlignmentSpecifierContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#declarator.
    def enterDeclarator(self, ctx:C11Parser.DeclaratorContext):
        try:
            identifier = ctx.IDENTIFIER()
            identifier = identifier.symbol  

        
            act_token = ShortToken(identifier.text, identifier.line, identifier.column)

            declarator_node = ECSTNode(uuid.uuid4(), self.current_node, act_token,'DECLARATOR')

            self.current_node.add_child(declarator_node)
            self.current_node = declarator_node

        except AttributeError:
            act_token = ShortToken('',-1, -1)
            declarator_node = ECSTNode(uuid.uuid4(), self.current_node, act_token,'DECLARATOR')
            self.current_node.add_child(declarator_node)
            self.current_node = declarator_node

    # Exit a parse tree produced by C11Parser#declarator.
    def exitDeclarator(self, ctx:C11Parser.DeclaratorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#directDeclarator.
    def enterDirectDeclarator(self, ctx:C11Parser.DirectDeclaratorContext):
        try:
            token = ctx.IDENTIFIER()
            token = token.symbol()
            
            act_token = ShortToken(token.text,token.line,token.column)
        except AttributeError:
            act_token = ShortToken(-1,-1)
            
        declarator_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'DIRECT_DECLARATOR')
        
        self.current_node.add_child(declarator_node)
        self.current_node = declarator_node

    # Exit a parse tree produced by C11Parser#directDeclarator.
    def exitDirectDeclarator(self, ctx:C11Parser.DirectDeclaratorContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#vcSpecificModifer.
    def enterVcSpecificModifer(self, ctx:C11Parser.VcSpecificModiferContext):
        pass

    # Exit a parse tree produced by C11Parser#vcSpecificModifer.
    def exitVcSpecificModifer(self, ctx:C11Parser.VcSpecificModiferContext):
        pass


    # Enter a parse tree produced by C11Parser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:C11Parser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by C11Parser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:C11Parser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by C11Parser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:C11Parser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by C11Parser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:C11Parser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by C11Parser#gccAttributeList.
    def enterGccAttributeList(self, ctx:C11Parser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by C11Parser#gccAttributeList.
    def exitGccAttributeList(self, ctx:C11Parser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by C11Parser#gccAttribute.
    def enterGccAttribute(self, ctx:C11Parser.GccAttributeContext):
        pass

    # Exit a parse tree produced by C11Parser#gccAttribute.
    def exitGccAttribute(self, ctx:C11Parser.GccAttributeContext):
        pass


    # Enter a parse tree produced by C11Parser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:C11Parser.NestedParenthesesBlockContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        nested_parentheses_block_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'NESTED_PARENTHESES_BLOCK')
    
        self.current_node.add_child(nested_parentheses_block_node)
        self.current_node = nested_parentheses_block_node

    # Exit a parse tree produced by C11Parser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:C11Parser.NestedParenthesesBlockContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#pointer.
    def enterPointer(self, ctx:C11Parser.PointerContext):
        act_token = ShortToken('',0,0)
        pointer_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'POINTER')
        self.current_node.add_child(pointer_node)
        self.current_node = pointer_node

    # Exit a parse tree produced by C11Parser#pointer.
    def exitPointer(self, ctx:C11Parser.PointerContext):
        self.current_node = self.current_node.parent

    # Const,Volatile,Atomic,Restricted,etc...
    # Enter a parse tree produced by C11Parser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:C11Parser.TypeQualifierListContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        type_qualifier_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'TYPE_QUALIFIER_LIST')
        
        self.current_node.add_child(type_qualifier_list_node)
        self.current_node = type_qualifier_list_node

    # Exit a parse tree produced by C11Parser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:C11Parser.TypeQualifierListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#parameterTypeList.
    def enterParameterTypeList(self, ctx:C11Parser.ParameterTypeListContext):
        act_token = ShortToken('', ctx.start.line,ctx.start.column)
        
        parameter_type_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'PARAMETER_TYPE_LIST')
        
        self.current_node.add_child(parameter_type_list_node)
        self.current_node = parameter_type_list_node

    # Exit a parse tree produced by C11Parser#parameterTypeList.
    def exitParameterTypeList(self, ctx:C11Parser.ParameterTypeListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#parameterList.
    def enterParameterList(self, ctx:C11Parser.ParameterListContext):
        act_token = ShortToken('', 0, 0)
        parameter_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'VALUE_ARGUMENT_LIST')
        self.current_node.add_child(parameter_node)
        self.current_node = parameter_node

    # Exit a parse tree produced by C11Parser#parameterList.
    def exitParameterList(self, ctx:C11Parser.ParameterListContext):
        self.current_node = self.current_node.parent



    # Enter a parse tree produced by C11Parser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:C11Parser.ParameterDeclarationContext):
        act_token = ShortToken('', ctx.start.line,ctx.start.column)
        
        parameter_declaration_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'PARAMETER_DECLARATION')
        
        self.current_node.add_child(parameter_declaration_node)
        self.current_node = parameter_declaration_node

    # Exit a parse tree produced by C11Parser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:C11Parser.ParameterDeclarationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#identifierList.
    def enterIdentifierList(self, ctx:C11Parser.IdentifierListContext):
        try:
            #for identifier in ctx.IDENTIFIER()
            token = (ctx.IDENTIFIER())
            token = token.symbol
            act_token = ShortToken(token.text, token.line, token.column)
        except AttributeError:
            act_token = ShortToken('', -1, -1)
        identifier_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LITERAL')
        self.current_node.add_child(identifier_node)
        self.current_node = identifier_node

    # Exit a parse tree produced by C11Parser#identifierList.
    def exitIdentifierList(self, ctx:C11Parser.IdentifierListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#typeName.
    def enterTypeName(self, ctx:C11Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by C11Parser#typeName.
    def exitTypeName(self, ctx:C11Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by C11Parser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:C11Parser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by C11Parser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:C11Parser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by C11Parser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:C11Parser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by C11Parser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:C11Parser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by C11Parser#typedefName.
    def enterTypedefName(self, ctx:C11Parser.TypedefNameContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        typedef_name_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'TYPEDEF_NAME')
        self.current_node.add_child(typedef_name_node)
        self.current_node = typedef_name_node

    # Exit a parse tree produced by C11Parser#typedefName.
    def exitTypedefName(self, ctx:C11Parser.TypedefNameContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#initializer.
    def enterInitializer(self, ctx:C11Parser.InitializerContext):
        if ctx.assignmentExpression():
            expression = ctx.assignmentExpression().getText()
            act_token = ShortToken(expression,ctx.start.line,ctx.start.column)
            
            expression_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ASSIGNMENT_EXPRESSION')
            
            self.current_node.add_child(expression_node)
            #self.current_node = expression_node
            
        elif ctx.initializerList():
            initializer_list = ctx.initializerList()
            for init in initializer_list:
                init_text = init.getText()
                act_token = ShortToken(init_text,ctx.start.line,ctx.start.column)
                
                init_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'INITIALIZER_LIST')
                self.current_node.add_child(init_node)
        else:
            init_text = ctx.getText()
            act_token = ShortToken(init_text,ctx.start.line,ctx.start.column)
            
            init_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'INITIALIZER')
            
            self.current_node.add_child(init_node)   
            self.current_node = init_node  
        
    # Exit a parse tree produced by C11Parser#initializer.
    def exitInitializer(self, ctx:C11Parser.InitializerContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#initializerList.
    def enterInitializerList(self, ctx:C11Parser.InitializerListContext):
        for initializer in initializerList:
            init_text = initializer.getText()
            act_token = ShortToken(init_text,ctx.start.line,ctx.start.column)
            
            init_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'INITIALIZER')
            
            self.current_node.add_child(init_node)
            self.current_node = init_node

    # Exit a parse tree produced by C11Parser#initializerList.
    def exitInitializerList(self, ctx:C11Parser.InitializerListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#designation.
    def enterDesignation(self, ctx:C11Parser.DesignationContext):
        pass

    # Exit a parse tree produced by C11Parser#designation.
    def exitDesignation(self, ctx:C11Parser.DesignationContext):
        pass


    # Enter a parse tree produced by C11Parser#designatorList.
    def enterDesignatorList(self, ctx:C11Parser.DesignatorListContext):
        pass

    # Exit a parse tree produced by C11Parser#designatorList.
    def exitDesignatorList(self, ctx:C11Parser.DesignatorListContext):
        pass


    # Enter a parse tree produced by C11Parser#designator.
    def enterDesignator(self, ctx:C11Parser.DesignatorContext):
        pass

    # Exit a parse tree produced by C11Parser#designator.
    def exitDesignator(self, ctx:C11Parser.DesignatorContext):
        pass


    # Enter a parse tree produced by C11Parser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:C11Parser.StaticAssertDeclarationContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        static_assert_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'ASSERT')
        
        self.current_node.add_child(static_assert_node)
        self.current_node = static_assert_node

    # Exit a parse tree produced by C11Parser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:C11Parser.StaticAssertDeclarationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#statement.
    def enterStatement(self, ctx:C11Parser.StatementContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'EXPRESSION')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by C11Parser#statement.
    def exitStatement(self, ctx:C11Parser.StatementContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#labeledStatement.
    def enterLabeledStatement(self, ctx:C11Parser.LabeledStatementContext):
        act_token = ShortToken('', ctx.start.line, ctx.start.column)

        # cvor za labelisani statement
        labeled_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LABELED_STATEMENT'
        )

        # labela
        label_node = ECSTNode(
            str(uuid.uuid4()), labeled_node, act_token,'LABEL', label=ctx.identifier().getText())  
        labeled_node.add_child(label_node)
        self.current_node.add_child(labeled_node)
        self.current_node = labeled_node

    # Exit a parse tree produced by C11Parser#labeledStatement.
    def exitLabeledStatement(self, ctx:C11Parser.LabeledStatementContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#compoundStatement.
    def enterCompoundStatement(self, ctx:C11Parser.CompoundStatementContext):
        if self.current_node.type == 'FUNCTION_DECL':
            act_token = ShortToken('', 0, 0)
            compound_node = ECSTNode(
                str(uuid.uuid4()), self.current_node, act_token,
                'FUNCTION_BODY')
            self.current_node.add_child(compound_node)
            self.current_node = compound_node
        

    # Exit a parse tree produced by C11Parser#compoundStatement.
    def exitCompoundStatement(self, ctx:C11Parser.CompoundStatementContext):
        if self.current_node.parent.type == 'FUNCTION_DECL':
            self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#blockItemList.
    def enterBlockItemList(self, ctx:C11Parser.BlockItemListContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        block_item_list_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'COLLECTION')
        
        self.current_node.add_child(block_item_list_node)
        self.current_node = block_item_list_node

    # Exit a parse tree produced by C11Parser#blockItemList.
    def exitBlockItemList(self, ctx:C11Parser.BlockItemListContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#blockItem.
    def enterBlockItem(self, ctx:C11Parser.BlockItemContext):
        pass

    # Exit a parse tree produced by C11Parser#blockItem.
    def exitBlockItem(self, ctx:C11Parser.BlockItemContext):
        pass


    # Enter a parse tree produced by C11Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:C11Parser.ExpressionStatementContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        expression_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'EXPRESSION')
        
        self.current_node.add_child(expression_node)
        self.current_node = expression_node

    # Exit a parse tree produced by C11Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:C11Parser.ExpressionStatementContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#selectionStatement.
    def enterSelectionStatement(self, ctx:C11Parser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by C11Parser#selectionStatement.
    def exitSelectionStatement(self, ctx:C11Parser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by C11Parser#iterationStatement.
    def enterIterationStatement(self, ctx:C11Parser.IterationStatementContext):
        act_token = ShortToken('',ctx.start.line,ctx.start.column)
        
        iteration_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'LOOP_STATEMENT')
        
        self.current_node.add_child(iteration_node)
        self.current_node = iteration_node

    # Exit a parse tree produced by C11Parser#iterationStatement.
    def exitIterationStatement(self, ctx:C11Parser.IterationStatementContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#forCondition.
    def enterForCondition(self, ctx:C11Parser.ForConditionContext):
        act_token = ShortToken('',0,0)
        condition_node = ECSTNode(str(uuid.uuid4),self.current_node,act_token,'FOR_CONDITION')
        self.current_node.add_child(condition_node)
        self.current_node = condition_node

    # Exit a parse tree produced by C11Parser#forCondition.
    def exitForCondition(self, ctx:C11Parser.ForConditionContext):
        self.current_node = self.current_node.parent



    # Enter a parse tree produced by C11Parser#forDeclaration.
    def enterForDeclaration(self, ctx:C11Parser.ForDeclarationContext):
        #v1 ->pocetni template
        #act_token = ShortToken('', 0, 0)
        #file_node = ECSTNode(
        #    str(uuid.uuid4()), self.current_node, act_token,
        #    'VARIABLE_DECL')
        #self.current_node.add_child(file_node)
        #self.current_node = file_node
        
        act_token = ShortToken('', ctx.start.line, ctx.start.column)
        for_declaration_node = ECSTNode(uuid.uuid4(),self.current_node,act_token,'FOR_DECLARATION')
        self.current_node.add_child(for_declaration_node)
        self.current_node = for_declaration_node


    # Exit a parse tree produced by C11Parser#forDeclaration.
    def exitForDeclaration(self, ctx:C11Parser.ForDeclarationContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#forExpression.
    def enterForExpression(self, ctx:C11Parser.ForExpressionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'LOOP_STATEMENT')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by C11Parser#forExpression.
    def exitForExpression(self, ctx:C11Parser.ForExpressionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#jumpStatement.
    def enterJumpStatement(self, ctx:C11Parser.JumpStatementContext):
        act_token = ShortToken('', ctx.start.line, ctx.start.column)

        # proveri tip 
        if ctx.BREAK():
            jump_type = 'BREAK'
        elif ctx.CONTINUE():
            jump_type = 'CONTINUE'
        elif ctx.RETURN():
            jump_type = 'RETURN'
        elif ctx.GOTO():
            jump_type = 'GOTO'
        else:
            jump_type = 'UNKNOWN_JUMP'

        jump_node = ECSTNode(str(uuid.uuid4()), self.current_node, act_token,jump_type)

        self.current_node.add_child(jump_node)
        self.current_node = jump_node

    # Exit a parse tree produced by C11Parser#jumpStatement.
    def exitJumpStatement(self, ctx:C11Parser.JumpStatementContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#compilationUnit.
    def enterCompilationUnit(self, ctx:C11Parser.CompilationUnitContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token, 'FILE')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by C11Parser#compilationUnit.
    def exitCompilationUnit(self, ctx:C11Parser.CompilationUnitContext):
        self.current_node = self.current_node.parent
        


    # Enter a parse tree produced by C11Parser#translationUnit.
    def enterTranslationUnit(self, ctx:C11Parser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by C11Parser#translationUnit.
    def exitTranslationUnit(self, ctx:C11Parser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by C11Parser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:C11Parser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by C11Parser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:C11Parser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by C11Parser#functionDefinition.
    def enterFunctionDefinition(self, ctx:C11Parser.FunctionDefinitionContext):
        act_token = ShortToken('', 0, 0)
        file_node = ECSTNode(
            str(uuid.uuid4()), self.current_node, act_token,
            'FUNCTION_DECL')
        self.current_node.add_child(file_node)
        self.current_node = file_node

    # Exit a parse tree produced by C11Parser#functionDefinition.
    def exitFunctionDefinition(self, ctx:C11Parser.FunctionDefinitionContext):
        self.current_node = self.current_node.parent


    # Enter a parse tree produced by C11Parser#declarationList.
    def enterDeclarationList(self, ctx:C11Parser.DeclarationListContext):
        pass

    # Exit a parse tree produced by C11Parser#declarationList.
    def exitDeclarationList(self, ctx:C11Parser.DeclarationListContext):
        pass



del C11Parser