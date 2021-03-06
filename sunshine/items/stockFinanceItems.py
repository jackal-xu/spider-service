#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: jaxon
@Time: 2021-01-22 22:27
"""

from scrapy.item import Item, Field


class StockFinanceAnalysis(Item):
    SecuCode = Field()
    AnnDate = Field()  #公告日期
    EndDate = Field()  #报告期
    EPS = Field()  # 基本每股收益
    DtEPS = Field()  # 稀释每股收益
    TotalRevenuePS = Field()  # 每股营业总收入
    RevenuePS = Field()  # 每股营业收入
    CapitalResePS = Field()  # 每股资本公积
    SurplusResePS = Field()  # 每股盈余公积
    UndistProfitPS = Field()  # 每股未分配利润
    ExtraItem = Field()  # 非经常性损益
    ProfitDedt = Field()  # 扣除非经常性损益后的净利润
    GrossMargin = Field()  # 毛利
    CurrentRatio = Field()  # 流动比率
    QuickRatio = Field()  # 速动比率
    CashRatio = Field()  # 保守速动比率
    InvturnDays = Field()  # 存货周转天数
    ArturnDays = Field()  # 应收账款周转天数
    InvTurn = Field()  # 存货周转率
    ArTurn = Field()  # 应收账款周转率
    CaTurn = Field()   # 流动资产周转率
    FaTurn = Field()  # 固定资产周转率
    AssetsTurn = Field()  # 总资产周转率
    OpIncome = Field()  # 经营活动净收益
    ValuechangeIncome = Field()  # 价值变动净收益
    InterstIncome = Field()  # 利息费用
    Daa = Field()  # 折旧与摊销
    Ebit = Field()  # 息税前利润
    Ebitda = Field()  # 息税折旧摊销前利润
    Fcff = Field()  # 企业自由现金流量
    Fcfe = Field()  # 股权自由现金流量
    CurrentExint = Field()  # 无息流动负债
    NoncurrentExint = Field()  # 无息非流动负债
    Interestdebt = Field()  # 带息债务
    Netdebt = Field()  # 净债务
    TangibleAsset = Field() #有形资产
    WorkingCapital = Field() #营运资金
    NetworkingCapital = Field() #营运流动资本
    invest_capital = Field() #全部投入资本
    retained_earnings = Field() #留存收益
    diluted2_eps = Field() #期末摊薄每股收益
    bps = Field() #每股净资产
    ocfps = Field() #每股经营活动产生的现金流量净额
    retainedps = Field() #每股留存收益
    cfps = Field() #每股现金流量净额
    ebit_ps = Field() #每股息税前利润
    fcff_ps = Field() #每股企业自由现金流量
    fcfe_ps = Field() #每股股东自由现金流量
    netprofit_margin = Field() #销售净利率
    grossprofit_margin = Field() #销售毛利率
    cogs_of_sales = Field() #销售成本率
    expense_of_sales = Field() #销售期间费用率
    profit_to_gr = Field() #净利润 / 营业总收入
    saleexp_to_gr = Field() #销售费用 / 营业总收入
    adminexp_of_gr = Field() #管理费用 / 营业总收入
    finaexp_of_gr = Field() #财务费用 / 营业总收入
    impai_ttm = Field() #资产减值损失 / 营业总收入
    gc_of_gr = Field() #营业总成本 / 营业总收入
    op_of_gr = Field() #营业利润 / 营业总收入
    ebit_of_gr = Field() #息税前利润 / 营业总收入
    roe = Field() #净资产收益率
    roe_waa = Field() #加权平均净资产收益率
    roe_dt = Field() #净资产收益率(扣除非经常损益)
    roa = Field() #总资产报酬率
    npta = Field() #总资产净利润
    roic = Field() #投入资本回报率
    roe_yearly = Field() #年化净资产收益率
    roa2_yearly = Field() #年化总资产报酬率
    roe_avg = Field() #平均净资产收益率(增发条件)
    opincome_of_ebt = Field() #经营活动净收益 / 利润总额
    investincome_of_ebt = Field() #价值变动净收益 / 利润总额
    n_op_profit_of_ebt = Field() #营业外收支净额 / 利润总额
    tax_to_ebt = Field() #所得税 / 利润总额
    dtprofit_to_profit = Field() #扣除非经常损益后的净利润 / 净利润
    salescash_to_or = Field() #销售商品提供劳务收到的现金 / 营业收入
    ocf_to_or = Field() #经营活动产生的现金流量净额 / 营业收入
    ocf_to_opincome = Field() #经营活动产生的现金流量净额 / 经营活动净收益
    capitalized_to_da = Field() #资本支出 / 折旧和摊销
    debt_to_assets = Field() #资产负债率
    assets_to_eqt = Field() #权益乘数
    dp_assets_to_eqt = Field() #权益乘数(杜邦分析)
    ca_to_assets = Field() #流动资产 / 总资产
    nca_to_assets = Field() #非流动资产 / 总资产
    tbassets_to_totalassets = Field() #有形资产 / 总资产
    int_to_talcap = Field() #带息债务 / 全部投入资本
    eqt_to_talcapital = Field() #归属于母公司的股东权益 / 全部投入资本
    currentdebt_to_debt = Field() #流动负债 / 负债合计
    longdeb_to_debt = Field() #非流动负债 / 负债合计
    ocf_to_shortdebt = Field() #经营活动产生的现金流量净额 / 流动负债
    debt_to_eqt = Field() #产权比率
    eqt_to_debt = Field() #归属于母公司的股东权益 / 负债合计
    eqt_to_interestdebt = Field() #归属于母公司的股东权益 / 带息债务
    tangibleasset_to_debt = Field() #有形资产 / 负债合计
    tangasset_to_intdebt = Field() #有形资产 / 带息债务
    tangibleasset_to_netdebt = Field() #有形资产 / 净债务
    ocf_to_debt = Field() #经营活动产生的现金流量净额 / 负债合计
    ocf_to_interestdebt = Field() #经营活动产生的现金流量净额 / 带息债务
    ocf_to_netdebt = Field() #经营活动产生的现金流量净额 / 净债务
    ebit_to_interest = Field() #已获利息倍数(EBIT / 利息费用)
    longdebt_to_workingcapital = Field() #长期债务与营运资金比率
    ebitda_to_debt = Field() #息税折旧摊销前利润 / 负债合计
    turn_days = Field() #营业周期
    roa_yearly = Field() #年化总资产净利率
    roa_dp = Field() #总资产净利率(杜邦分析)
    fixed_assets = Field() #固定资产合计
    profit_prefin_exp = Field() #扣除财务费用前营业利润
    non_op_profit = Field() #非营业利润
    op_to_ebt = Field() #营业利润／利润总额
    nop_to_ebt = Field() #非营业利润／利润总额
    ocf_to_profit = Field() #经营活动产生的现金流量净额／营业利润
    cash_to_liqdebt = Field() #货币资金／流动负债
    cash_to_liqdebt_withinterest = Field() #货币资金／带息流动负债
    op_to_liqdebt = Field() #营业利润／流动负债
    op_to_debt = Field() #营业利润／负债合计
    roic_yearly = Field() #年化投入资本回报率
    total_fa_trun = Field() #固定资产合计周转率
    profit_to_op = Field() #利润总额／营业收入
    q_opincome = Field() #经营活动单季度净收益
    q_investincome = Field() #价值变动单季度净收益
    q_dtprofit = Field() #扣除非经常损益后的单季度净利润
    q_eps = Field() #每股收益(单季度)
    q_netprofit_margin = Field() #销售净利率(单季度)
    q_gsprofit_margin = Field() #销售毛利率(单季度)
    q_exp_to_sales = Field() #销售期间费用率(单季度)
    q_profit_to_gr = Field() #净利润／营业总收入(单季度)
    q_saleexp_to_gr = Field() #销售费用／营业总收入(单季度)
    q_adminexp_to_gr = Field() #管理费用／营业总收入(单季度)
    q_finaexp_to_gr = Field() #财务费用／营业总收入(单季度)
    q_impair_to_gr_ttm = Field() #资产减值损失／营业总收入(单季度)
    q_gc_to_gr = Field() #营业总成本／营业总收入(单季度)
    q_op_to_gr = Field() #营业利润／营业总收入(单季度)
    q_roe = Field() #净资产收益率(单季度)
    q_dt_roe = Field() #净资产单季度收益率(扣除非经常损益)
    q_npta = Field()  # 总资产净利润(单季度)
    q_opincome_to_ebt = Field()  # 经营活动净收益／利润总额(单季度)
    q_investincome_to_ebt = Field()  # 价值变动净收益／利润总额(单季度)
    q_dtprofit_to_profit = Field()  # 扣除非经常损益后的净利润／净利润(单季度)
    q_salescash_to_or = Field()  # 销售商品提供劳务收到的现金／营业收入(单季度)
    q_ocf_to_sales = Field()  # 经营活动产生的现金流量净额／营业收入(单季度)
    q_ocf_to_or = Field()  # 经营活动产生的现金流量净额／经营活动净收益(单季度)
    basic_eps_yoy = Field()  # 基本每股收益同比增长率( %)
    dt_eps_yoy = Field()  # 稀释每股收益同比增长率( %)
    cfps_yoy = Field()  # 每股经营活动产生的现金流量净额同比增长率( %)
    op_yoy = Field()  # 营业利润同比增长率( %)
    ebt_yoy = Field()  # 利润总额同比增长率( %)
    netprofit_yoy = Field()  # 归属母公司股东的净利润同比增长率( %)
    dt_netprofit_yoy = Field()  # 归属母公司股东的净利润 - 扣除非经常损益同比增长率( %)
    ocf_yoy = Field()  # 经营活动产生的现金流量净额同比增长率( %)
    roe_yoy = Field()  # 净资产收益率(摊薄)同比增长率( %)
    bps_yoy = Field()  # 每股净资产相对年初增长率( %)
    assets_yoy = Field()  # 资产总计相对年初增长率( %)
    eqt_yoy = Field()  # 归属母公司的股东权益相对年初增长率( %)
    tr_yoy = Field()  # 营业总收入同比增长率( %)
    or_yoy = Field()  # 营业收入同比增长率( %)
    q_gr_yoy = Field()  # 营业总收入同比增长率( %)(单季度)
    q_gr_qoq = Field()  # 营业总收入环比增长率( %)(单季度)
    q_sales_yoy = Field()  # 营业收入同比增长率( %)(单季度)
    q_sales_qoq = Field()  # 营业收入环比增长率( %)(单季度)
    q_op_yoy = Field()  # 营业利润同比增长率( %)(单季度)
    q_op_qoq = Field()  # 营业利润环比增长率( %)(单季度)
    q_profit_yoy = Field()  # 净利润同比增长率( %)(单季度)
    q_profit_qoq = Field()  # 净利润环比增长率( %)(单季度)
    q_netprofit_yoy = Field()  # 归属母公司股东的净利润同比增长率( %)(单季度)
    q_netprofit_qoq = Field()  # 归属母公司股东的净利润环比增长率( %)(单季度)
    equity_yoy = Field()  # 净资产同比增长率
    rd_exp = Field()  # 研发费用
    update_flag = Field()  # 更新标识
    