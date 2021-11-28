# Generated from C:/Users/roque/Downloads/programming/PycharmProjects/P2Grammar\grammatica.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u0089\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2*\n\2\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\rd\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"\2\2\2\u0082\2)\3\2\2\2\4\60\3\2\2\2\6\62\3\2\2")
        buf.write("\2\b>\3\2\2\2\nA\3\2\2\2\fH\3\2\2\2\16K\3\2\2\2\20P\3")
        buf.write("\2\2\2\22U\3\2\2\2\24Y\3\2\2\2\26[\3\2\2\2\30c\3\2\2\2")
        buf.write("\32e\3\2\2\2\34p\3\2\2\2\36{\3\2\2\2 \u0083\3\2\2\2\"")
        buf.write("\u0086\3\2\2\2$*\5\4\3\2%*\5\24\13\2&*\5\30\r\2\'*\7\31")
        buf.write("\2\2(*\7\30\2\2)$\3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'\3\2\2")
        buf.write("\2)(\3\2\2\2*\3\3\2\2\2+\61\5\6\4\2,\61\5\b\5\2-\61\5")
        buf.write("\n\6\2.\61\5\f\7\2/\61\5\16\b\2\60+\3\2\2\2\60,\3\2\2")
        buf.write("\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\5\3\2\2\2\62")
        buf.write("\63\7\3\2\2\63\64\5\2\2\2\648\7\4\2\2\65\67\5\20\t\2\66")
        buf.write("\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2")
        buf.write("\2:8\3\2\2\2;<\5\22\n\2<=\7\5\2\2=\7\3\2\2\2>?\7\6\2\2")
        buf.write("?@\5\2\2\2@\t\3\2\2\2AB\7\7\2\2BC\5\2\2\2CD\7\b\2\2DE")
        buf.write("\7\4\2\2EF\5\22\n\2FG\7\5\2\2G\13\3\2\2\2HI\7\t\2\2IJ")
        buf.write("\5\2\2\2J\r\3\2\2\2KL\7\n\2\2LM\5\2\2\2MN\7\13\2\2NO\5")
        buf.write("\2\2\2O\17\3\2\2\2PQ\5\2\2\2QR\7\f\2\2RS\5\2\2\2ST\7\r")
        buf.write("\2\2T\21\3\2\2\2UV\5\2\2\2VW\7\f\2\2WX\5\2\2\2X\23\3\2")
        buf.write("\2\2YZ\5\26\f\2Z\25\3\2\2\2[\\\7\16\2\2\\]\5\2\2\2]^\7")
        buf.write("\17\2\2^_\5\2\2\2_\27\3\2\2\2`d\5\32\16\2ad\5\34\17\2")
        buf.write("bd\5\36\20\2c`\3\2\2\2ca\3\2\2\2cb\3\2\2\2d\31\3\2\2\2")
        buf.write("ef\7\20\2\2fg\7\21\2\2gh\5\2\2\2hi\7\4\2\2ij\5\"\22\2")
        buf.write("jk\7\5\2\2kl\7\22\2\2lm\7\4\2\2mn\5\"\22\2no\7\5\2\2o")
        buf.write("\33\3\2\2\2pq\7\23\2\2qr\5\2\2\2rs\7\24\2\2st\5\2\2\2")
        buf.write("tu\7\25\2\2uv\5\2\2\2vw\7\26\2\2wx\5\2\2\2xy\7\25\2\2")
        buf.write("yz\5\2\2\2z\35\3\2\2\2{|\7\27\2\2|}\7\17\2\2}~\5\2\2\2")
        buf.write("~\177\7\26\2\2\177\u0080\5\2\2\2\u0080\u0081\7\25\2\2")
        buf.write("\u0081\u0082\5\2\2\2\u0082\37\3\2\2\2\u0083\u0084\5\2")
        buf.write("\2\2\u0084\u0085\7\r\2\2\u0085!\3\2\2\2\u0086\u0087\5")
        buf.write("\2\2\2\u0087#\3\2\2\2\6)\608c")
        return buf.getvalue()


class grammaticaParser ( Parser ):

    grammarFileName = "grammatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'('", "')'", "'DROP'", "'ALTER'", 
                     "'ADD'", "'TRUNCATE'", "'RENAME'", "'TO'", "':'", "','", 
                     "'SELECT'", "'FROM'", "'INSERT'", "'INTO'", "'VALUES'", 
                     "'UPDATE'", "'SET'", "'='", "'WHERE'", "'DELETE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STR", "INT", "WS" ]

    RULE_expr = 0
    RULE_ddl = 1
    RULE_create = 2
    RULE_drop = 3
    RULE_alter = 4
    RULE_truncate = 5
    RULE_rename = 6
    RULE_mittlal = 7
    RULE_terminal = 8
    RULE_dql = 9
    RULE_select = 10
    RULE_sql = 11
    RULE_insert = 12
    RULE_update = 13
    RULE_delete = 14
    RULE_smallmittlal = 15
    RULE_smallterminal = 16

    ruleNames =  [ "expr", "ddl", "create", "drop", "alter", "truncate", 
                   "rename", "mittlal", "terminal", "dql", "select", "sql", 
                   "insert", "update", "delete", "smallmittlal", "smallterminal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    STR=22
    INT=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SqlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sql(self):
            return self.getTypedRuleContext(grammaticaParser.SqlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlExpr" ):
                listener.enterSqlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlExpr" ):
                listener.exitSqlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlExpr" ):
                return visitor.visitSqlExpr(self)
            else:
                return visitor.visitChildren(self)


    class StrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(grammaticaParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrExpr" ):
                listener.enterStrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrExpr" ):
                listener.exitStrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrExpr" ):
                return visitor.visitStrExpr(self)
            else:
                return visitor.visitChildren(self)


    class DqlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dql(self):
            return self.getTypedRuleContext(grammaticaParser.DqlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDqlExpr" ):
                listener.enterDqlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDqlExpr" ):
                listener.exitDqlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDqlExpr" ):
                return visitor.visitDqlExpr(self)
            else:
                return visitor.visitChildren(self)


    class DdlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ddl(self):
            return self.getTypedRuleContext(grammaticaParser.DdlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdlExpr" ):
                listener.enterDdlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdlExpr" ):
                listener.exitDdlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdlExpr" ):
                return visitor.visitDdlExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(grammaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = grammaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__0, grammaticaParser.T__3, grammaticaParser.T__4, grammaticaParser.T__6, grammaticaParser.T__7]:
                localctx = grammaticaParser.DdlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.ddl()
                pass
            elif token in [grammaticaParser.T__11]:
                localctx = grammaticaParser.DqlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.dql()
                pass
            elif token in [grammaticaParser.T__13, grammaticaParser.T__16, grammaticaParser.T__20]:
                localctx = grammaticaParser.SqlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.sql()
                pass
            elif token in [grammaticaParser.INT]:
                localctx = grammaticaParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                localctx.atom = self.match(grammaticaParser.INT)
                pass
            elif token in [grammaticaParser.STR]:
                localctx = grammaticaParser.StrExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                localctx.atom = self.match(grammaticaParser.STR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DdlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(grammaticaParser.CreateContext,0)


        def drop(self):
            return self.getTypedRuleContext(grammaticaParser.DropContext,0)


        def alter(self):
            return self.getTypedRuleContext(grammaticaParser.AlterContext,0)


        def truncate(self):
            return self.getTypedRuleContext(grammaticaParser.TruncateContext,0)


        def rename(self):
            return self.getTypedRuleContext(grammaticaParser.RenameContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_ddl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdl" ):
                listener.enterDdl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdl" ):
                listener.exitDdl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdl" ):
                return visitor.visitDdl(self)
            else:
                return visitor.visitChildren(self)




    def ddl(self):

        localctx = grammaticaParser.DdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ddl)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.create()
                pass
            elif token in [grammaticaParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.drop()
                pass
            elif token in [grammaticaParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.alter()
                pass
            elif token in [grammaticaParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.truncate()
                pass
            elif token in [grammaticaParser.T__7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.rename()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.pairs = None # MittlalContext
            self.pair = None # TerminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def terminal(self):
            return self.getTypedRuleContext(grammaticaParser.TerminalContext,0)


        def mittlal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.MittlalContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.MittlalContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate" ):
                return visitor.visitCreate(self)
            else:
                return visitor.visitChildren(self)




    def create(self):

        localctx = grammaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(grammaticaParser.T__0)
            self.state = 49
            localctx.name = self.expr()
            self.state = 50
            self.match(grammaticaParser.T__1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 51
                    localctx.pairs = self.mittlal() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 57
            localctx.pair = self.terminal()
            self.state = 58
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_drop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop" ):
                listener.enterDrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop" ):
                listener.exitDrop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrop" ):
                return visitor.visitDrop(self)
            else:
                return visitor.visitChildren(self)




    def drop(self):

        localctx = grammaticaParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_drop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(grammaticaParser.T__3)
            self.state = 61
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.pair = None # TerminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def terminal(self):
            return self.getTypedRuleContext(grammaticaParser.TerminalContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_alter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlter" ):
                listener.enterAlter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlter" ):
                listener.exitAlter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlter" ):
                return visitor.visitAlter(self)
            else:
                return visitor.visitChildren(self)




    def alter(self):

        localctx = grammaticaParser.AlterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(grammaticaParser.T__4)
            self.state = 64
            localctx.name = self.expr()
            self.state = 65
            self.match(grammaticaParser.T__5)
            self.state = 66
            self.match(grammaticaParser.T__1)
            self.state = 67
            localctx.pair = self.terminal()
            self.state = 68
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruncateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_truncate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncate" ):
                listener.enterTruncate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncate" ):
                listener.exitTruncate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncate" ):
                return visitor.visitTruncate(self)
            else:
                return visitor.visitChildren(self)




    def truncate(self):

        localctx = grammaticaParser.TruncateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_truncate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(grammaticaParser.T__6)
            self.state = 71
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.oldname = None # ExprContext
            self.newname = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_rename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRename" ):
                listener.enterRename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRename" ):
                listener.exitRename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRename" ):
                return visitor.visitRename(self)
            else:
                return visitor.visitChildren(self)




    def rename(self):

        localctx = grammaticaParser.RenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(grammaticaParser.T__7)
            self.state = 74
            localctx.oldname = self.expr()
            self.state = 75
            self.match(grammaticaParser.T__8)
            self.state = 76
            localctx.newname = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MittlalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExprContext
            self.value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_mittlal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMittlal" ):
                listener.enterMittlal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMittlal" ):
                listener.exitMittlal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMittlal" ):
                return visitor.visitMittlal(self)
            else:
                return visitor.visitChildren(self)




    def mittlal(self):

        localctx = grammaticaParser.MittlalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mittlal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            localctx.key = self.expr()
            self.state = 79
            self.match(grammaticaParser.T__9)
            self.state = 80
            localctx.value = self.expr()
            self.state = 81
            self.match(grammaticaParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExprContext
            self.value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)




    def terminal(self):

        localctx = grammaticaParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            localctx.key = self.expr()
            self.state = 84
            self.match(grammaticaParser.T__9)
            self.state = 85
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DqlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self):
            return self.getTypedRuleContext(grammaticaParser.SelectContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_dql

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDql" ):
                listener.enterDql(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDql" ):
                listener.exitDql(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDql" ):
                return visitor.visitDql(self)
            else:
                return visitor.visitChildren(self)




    def dql(self):

        localctx = grammaticaParser.DqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dql)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.select()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExprContext
            self.name = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = grammaticaParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(grammaticaParser.T__11)
            self.state = 90
            localctx.key = self.expr()
            self.state = 91
            self.match(grammaticaParser.T__12)
            self.state = 92
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def insert(self):
            return self.getTypedRuleContext(grammaticaParser.InsertContext,0)


        def update(self):
            return self.getTypedRuleContext(grammaticaParser.UpdateContext,0)


        def delete(self):
            return self.getTypedRuleContext(grammaticaParser.DeleteContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_sql

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql" ):
                listener.enterSql(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql" ):
                listener.exitSql(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql" ):
                return visitor.visitSql(self)
            else:
                return visitor.visitChildren(self)




    def sql(self):

        localctx = grammaticaParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sql)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.insert()
                pass
            elif token in [grammaticaParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.update()
                pass
            elif token in [grammaticaParser.T__20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.delete()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key = None # SmallterminalContext
            self.value = None # SmallterminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def smallterminal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.SmallterminalContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.SmallterminalContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_insert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert" ):
                listener.enterInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert" ):
                listener.exitInsert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert" ):
                return visitor.visitInsert(self)
            else:
                return visitor.visitChildren(self)




    def insert(self):

        localctx = grammaticaParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_insert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(grammaticaParser.T__13)
            self.state = 100
            self.match(grammaticaParser.T__14)
            self.state = 101
            localctx.name = self.expr()
            self.state = 102
            self.match(grammaticaParser.T__1)
            self.state = 103
            localctx.key = self.smallterminal()
            self.state = 104
            self.match(grammaticaParser.T__2)
            self.state = 105
            self.match(grammaticaParser.T__15)
            self.state = 106
            self.match(grammaticaParser.T__1)
            self.state = 107
            localctx.value = self.smallterminal()
            self.state = 108
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key1 = None # ExprContext
            self.key1value = None # ExprContext
            self.key2 = None # ExprContext
            self.key2value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = grammaticaParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(grammaticaParser.T__16)
            self.state = 111
            localctx.name = self.expr()
            self.state = 112
            self.match(grammaticaParser.T__17)
            self.state = 113
            localctx.key1 = self.expr()
            self.state = 114
            self.match(grammaticaParser.T__18)
            self.state = 115
            localctx.key1value = self.expr()
            self.state = 116
            self.match(grammaticaParser.T__19)
            self.state = 117
            localctx.key2 = self.expr()
            self.state = 118
            self.match(grammaticaParser.T__18)
            self.state = 119
            localctx.key2value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key = None # ExprContext
            self.value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete" ):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)




    def delete(self):

        localctx = grammaticaParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(grammaticaParser.T__20)
            self.state = 122
            self.match(grammaticaParser.T__12)
            self.state = 123
            localctx.name = self.expr()
            self.state = 124
            self.match(grammaticaParser.T__19)
            self.state = 125
            localctx.key = self.expr()
            self.state = 126
            self.match(grammaticaParser.T__18)
            self.state = 127
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmallmittlalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_smallmittlal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmallmittlal" ):
                listener.enterSmallmittlal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmallmittlal" ):
                listener.exitSmallmittlal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmallmittlal" ):
                return visitor.visitSmallmittlal(self)
            else:
                return visitor.visitChildren(self)




    def smallmittlal(self):

        localctx = grammaticaParser.SmallmittlalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_smallmittlal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            localctx.value = self.expr()
            self.state = 130
            self.match(grammaticaParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmallterminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_smallterminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmallterminal" ):
                listener.enterSmallterminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmallterminal" ):
                listener.exitSmallterminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmallterminal" ):
                return visitor.visitSmallterminal(self)
            else:
                return visitor.visitChildren(self)




    def smallterminal(self):

        localctx = grammaticaParser.SmallterminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_smallterminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





