# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Apr 16 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class betterNPV
###########################################################################

class betterNPV ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 590,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"initial investment\n" ), wx.HORIZONTAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"initial investment\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer4.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Discount rate \n", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		sbSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		gSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result\n" ), wx.VERTICAL )

		self.m_button1 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"NPV!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( sbSizer6, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"3 year cash flow" ), wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Type", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer8.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Income", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer8.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Expense", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer9.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer10.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer11.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer7.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.npv_calculate )
		self.m_button2.Bind( wx.EVT_BUTTON, self.clear_screen )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def npv_calculate( self, event ):
		event.Skip()

	def clear_screen( self, event ):
		event.Skip()


