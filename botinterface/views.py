# coding:utf-8



from django.http import HttpResponse

import sys, os, lucene
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.cn.smart import SmartChineseAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher




# Create your views here.
def index(request):
    vm_env = lucene.getVMEnv()
    if(vm_env):
        vm_env.attachCurrentThread()
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        directory = SimpleFSDirectory(Paths.get("/Users/css/nlplearn/yuliao/index1"))
        searcher = IndexSearcher(DirectoryReader.open(directory))
        ana = SmartChineseAnalyzer()
        command = "你好"
        query = QueryParser("question", ana).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        tmpdata = scoreDocs[0]
        doc = searcher.doc(tmpdata.doc)
        del searcher
        tmpresult = doc.get("answer").encode('utf-8')
        # print tmpresult
        response = HttpResponse(tmpresult)
        # response = HttpResponse('helloworld2')
        return response
    else:
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])
        #lucene.initVM()

        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        directory = SimpleFSDirectory(Paths.get("/Users/css/nlplearn/yuliao/index1"))
        searcher = IndexSearcher(DirectoryReader.open(directory))
        ana = SmartChineseAnalyzer()
        command="你好"
        query = QueryParser("question", ana).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        tmpdata=scoreDocs[0]
        doc = searcher.doc(tmpdata.doc)
        del searcher
        tmpresult=doc.get("answer").encode('utf-8')
        #print tmpresult
        response = HttpResponse(tmpresult)
        #response = HttpResponse('helloworld2')
        return response


