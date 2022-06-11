from score import *
#작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')
def sel_task(): #작업 선택 메뉴
    print("_"*50)
    print("1:검색 2:현황 3:통계 4:데이터관리 x:종료")
    selno = input("<작업 선택> ")
    if len(selno) == 0:
        return 'x'
    elif selno == 1:
        selmenu01_find()
    elif selno == 2:
        selmenu02_find()
    else:
        return selno


def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val #리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s 성명: %s 소속학과: %s(%s)" %(instid, sname, dname, deptid))