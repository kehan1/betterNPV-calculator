from betterNPV import *

class button_functions(betterNPV):
    def __init__(self, parent):
        betterNPV.__init__(self, parent) 

    def npv_calculate(self, event):
        input_valid = True
        try:
            investment = int(self.m_textCtrl1.GetValue()) 
            if (investment) < 0:
                input_valid = False
                wx.MessageBox("invalid investment number", "warn")
        except:
            wx.MessageBox("input investment number", "warn")
        

        try:
            rate = float(self.m_textCtrl2.GetValue())
            if(rate)<0:
                input_valid = False
                wx.MessageBox("invalid rate number", "warn")
        except:
            wx.MessageBox("invalid rate number", "warn")

        def pv_calculate(income, expense, rate, year):
                return float((income-expense)/((1+rate)**year))

        if input_valid:
            try:
                year1_income = float(self.m_textCtrl4.GetValue())
            except:
                year1_income = 0
            try:
                year1_expense = int(self.m_textCtrl5.GetValue())
            except:
                year1_expense = 0
            try:
                year2_income = int(self.m_textCtrl6.GetValue())
            except:
                year2_income =0
            try:
                year2_expense = int(self.m_textCtrl7.GetValue())
            except:
                year2_expense=0
            try:    
                year3_income = int(self.m_textCtrl8.GetValue())
            except:
                year3_income = 0
            try:
                year3_expense = int(self.m_textCtrl9.GetValue())
            except:
                year3_expense=0

            npv = -investment
            npv += pv_calculate(year1_income,year1_expense,rate,1)
            npv += pv_calculate(year2_income,year2_expense,rate,2)
            npv += pv_calculate(year3_income,year3_expense,rate,3)
            self.m_textCtrl3.SetValue (str('%.2f' % npv))

    
    def clear_screen(self, event):
       self.m_textCtrl1.Clear()
       self.m_textCtrl2.Clear()
       self.m_textCtrl3.Clear()
       self.m_textCtrl4.Clear()
       self.m_textCtrl5.Clear()
       self.m_textCtrl6.Clear()
       self.m_textCtrl7.Clear()
       self.m_textCtrl8.Clear()
       self.m_textCtrl9.Clear()


def main():
    app = wx.App()
    frame = button_functions(None).Show()
    app.MainLoop()

 
if __name__ == '__main__':
    main()

