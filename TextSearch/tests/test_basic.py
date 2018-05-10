from scrapper import requestm
import time

#https://eminwon.molit.go.kr/cmptReg.do?
#https://www.epeople.go.kr/jsp/user/frame/pc/cvreq/UPcCvreqForm.jsp?anc_code=1613000&channel=1613000&menu_code=PC001
sel = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20170322", "20180321", "개발부담금")
sel1 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20160322", "20170321", "개발부담금")
sel2 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20150322", "20160321", "개발부담금")
sel3 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20140322", "20150321", "개발부담금")
sel4 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20130322", "20140321", "개발부담금")
sel5 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20120322", "20130321", "개발부담금")
sel6 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20110322", "20120321", "개발부담금")
sel7 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20100322", "20110321", "개발부담금")
sel8 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20090322", "20100321", "개발부담금")
sel9 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20080322", "20090321", "개발부담금")

selC1 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20170322", "20180321", "")
selC2 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20160322", "20170321", "")
selC3 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20150322", "20160321", "")
selC4 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20140322", "20150321", "")
selC5 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20130322", "20140321", "")
selC6 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20120322", "20130321", "")
selC7 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20110322", "20120321", "")
selC8 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20100322", "20110321", "")
selC9 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20090322", "20100321", "")
selC10 = requestm.requestmanager("https://eminwon.molit.go.kr/cmptReg.do?", "20080322", "20090321", "")



#sel.start()
#sel1.start()
#sel2.start()
#sel3.start()
#sel4.start()
#sel5.start()
#sel6.start()
#sel7.start()
#sel8.start()
#sel9.start()

selC1.start()
selC2.start()
selC3.start()
selC4.start()
selC5.start()
#selC6.start()
#selC7.start()
#selC8.start()
#selC9.start()
#selC10.start()