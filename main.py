##TODO: from typing import List

from antlr4 import *
from gen.grammaticaLexer import grammaticaLexer
from gen.grammaticaParser import grammaticaParser
from gen.grammaticaVisitor import grammaticaVisitor

class MyVisitor(grammaticaVisitor):
    # def visitTemplate(self,ctx):
        # l = self.visit(ctx.left)
        # name = self.visit(ctx.name)
        # return something

    def visitNumberExpr(self, ctx):
        """
        Visitor instance for numbers (grammar expr: int)
        :param ctx: context
        :return: an integer
        """
        value = ctx.getText()
        return int(value)

    def visitStrExpr(self, ctx):
        """
        Visitor instance for strings (grammar expr: int)
        :param ctx: context
        :return: a string
        """
        value = ctx.getText()
        return str(value)

    def visitTerminal(self, ctx):
        """
        Visitor instance for a terminal (key:value pair in grammar)
        :param ctx: context
        :return: key, value pair
        """
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        return (key, value)

    def visitCreate(self, ctx):
        """
        Visitor instance for creation of a data object stored in db
        :param ctx: context
        :return: modified db
        """
        key, value = self.visit(ctx.pair)
        newdict = {key:value}
        db[self.visit(ctx.name)] = [newdict]
        return db

    def visitDrop(self, ctx):
        """
        Visitor instance that removes a data object from db
        :param ctx: context
        :return: modified db
        """
        db.pop(self.visit(ctx.name))
        return db

    def visitAlter(self, ctx):
        """
        Visitor instance that adds an item to a data object in db
        :param ctx: context
        :return: modified db
        """
        key, value = self.visit(ctx.pair)
        newdict = {key:value}
        db[self.visit(ctx.name)].append(newdict)
        return db

    def visitTruncate(self, ctx):
        """
        Visitor instance that truncates a data object from db
        :param ctx: context
        :return: modified db
        """
        if self.visit(ctx.name) in db:
            db[self.visit(ctx.name)] = []
        else:
            pass
        return db

    def visitRename(self, ctx):
        """
        Visitor instance that renames a data object in db
        :param ctx: context
        :return: modified db
        """
        db[self.visit(ctx.newname)] = db[self.visit(ctx.oldname)]
        db.pop(self.visit(ctx.oldname))
        return db

    def visitSelect(self, ctx):
        """
        Visitor instance that displays a specified field from a data object in db
        :param ctx: context
        :return: list of values
        """
        name = self.visit(ctx.name)
        key = self.visit(ctx.key)
        result = []
        for x in db[name]:
            if x[key]:
                result.append(x[key])
        return result

    def visitInsert(self, ctx):
        """
        Visitor instance that inserts a key and a value to an object in db
        :param ctx: context
        :return: modified db
        """
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        newdict = {key:value}
        db[self.visit(ctx.name)].append(newdict)
        return db

    def visitUpdate(self, ctx):
        """
        Visitor instance that updates old values in a data object in db
        :param ctx: context
        :return: modified db
        """
        key1 = self.visit(ctx.key1)
        key1value = self.visit(ctx.key1value)
        key2 = self.visit(ctx.key2)
        key2value = self.visit(ctx.key2value)
        for x in db[self.visit(ctx.name)]:
            if x[key2] == key2value:
                x[key1] = key1value
        return db

    def visitDelete(self, ctx):
        """
        Visitor instance that deletes items following a specified condition in db
        :param ctx: context
        :return: modified db
        """
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        for x in db[self.visit(ctx.name)]:
            if x[key] == value:
                db[self.visit(ctx.name)].remove(x)
        return db

if __name__ == "__main__":
    db = {} # data is stored in a dict
    while True:
        data = InputStream(input("> "))
        # lexer
        lexer = grammaticaLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = grammaticaParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output) # print db