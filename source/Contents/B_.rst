
Economica
=========

**计量经济学** -- 李子奈

https://www.bilibili.com/video/BV1Eb411B78w?p=1

Introduction
------------

经济理论 数学 与统计学 三者就是计量经济学

**科学研究**


* 观察 -- 偶然
* 假设 -- 理论 模型
* 检验 -- 实验，回归，预测

**经济学方法论**
^^^^^^^^^^^^^^^^^^^^


* 规范分析 normative 政治经济学 价值判断 不被重视
* 实证分析 positive

  * 理论分析 Theoretical 微观和宏观经济学
  * 经验分析 Empirical 计量经济学

实证方法--经验方法--回归分析

**计量经济学模型**
^^^^^^^^^^^^^^^^^^^^^^


* 物理模型
* 模拟模型
* 数学模型

  * 经济数学模型

    * 理论模型 -- 因素之间的关系
    * 经验模型 -- 定量关系

      * 计量经济模型

        * 截面数据模型 cross sectional
        * 时序数据模型 time series
        * 面板模型 panel data

      * 投入产出分析模型
      * 经济控制论模型
      * ...

**计量经济学模型的地位**


* 理论分析 -- 行为分析
* 数理分析 -- 函数关系
* 数量分析 -- 计量分析

**计量经济学内容体系**
^^^^^^^^^^^^^^^^^^^^^^^^^^


* 理论与应用
* 经典与非经典

  * 经典

    * ~1970s 单方程模型 联立方程模型
    * 理论导向 基于行为分析
    * 概率论作为方法基础
    * 识别、估计、检验 主要技术问题
    * 主要标准：拟合优度

  * 批判 Lucas批判

    * 理论导向 不同人的分析不同
    * 结构参数的不变性
    * Lucas(1976)、Sarget(1976)、Sims(1980)

  * 时代背景 --凯恩斯主义 -- 新古典宏观经济学: 宏观政策的有效性
    --新凯恩斯主义
  * 非经典

    * 微观、非参数、时间序列、动态 70s+

* 微观与宏观

  * 微观 面板数据模型、离散选择模型、选择性样本
  * 宏观

    * 经典 宏观经济模型
    * 非经典：时间序列经济学的宏观部分 协整理论 动态计量经济学

经济学是一种方法论


* 选择性样本而非随机抽样 Heckman
* 离散选择模型 被解释变量离散 McFadden
* 宏观时间序列分析 Granger
* ARCH 微观时间序列分析 Engle

建立计量经济学模型的步骤和要点
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

理论模型的建立
~~~~~~~~~~~~~~


* **确定模型包含的变量**

  * 依据理论、关系、数据选择变量
  * 不遗漏显著变量
  * 数据的可得性
  * **变量关系独立**

* 确定模型的数学形式

  * 利用理论成果
  * **根据样本数据做关系图**
  * 选择可能形式试模型

* 拟定模型中待估计参数的理论期望值区间

  * 符号 大小
  * 关系： 弹性和=0？

样本数据的收集
~~~~~~~~~~~~~~


* 常用样本数据

  * 截面数据
  * 时间序列
  * 离散数据

* 质量

  * 可比性 资本的时间价值
  * **一致性**\ ：从母体中抽取 煤炭行业与煤炭企业
  * 随机性：截面数据可以，时序数据不行 -- 对于时序数据的特殊处理

模型参数的估计
~~~~~~~~~~~~~~


* 各类模型

  * 最小二乘
  * 最大似然

* 如何选择模型参数估计方法

模型检验
~~~~~~~~


* **经济意义检验**\ ：根据拟定的符号、大小、关系。对参数估计结果进行可靠性判断
* 统计检验：由数理统计理论决定

  * 拟合优度检验
  * 总体显著性检验
  * 变量显著性检验

* 计量经济学检验：由计量经济学理论决定

  * 异方差性检验
  * 序列相关性检验
  * 共线性检验

* 模型预测检验：由模型应用决定

  * 稳定性检验：扩大样本重新估计
  * 预测性能检验：对样本外一点进行实际预测

应用
^^^^


* **结构分析**

  * 分析变量之间的关系
  * 弹性分析 扩大百分之多少
  * 乘数分析 多少倍
  * 比较静力分析

* 经济预测

  * 取决于经济现象是否稳定

* 政策评价

  * 经济政策的\ **不可实验性** 难以避免失误

Application
-----------

计量经济建模的常见问题
^^^^^^^^^^^^^^^^^^^^^^

步骤


* 选择变量

  * 样本一致性

    * 样本要能代表母体

  * 样本点间变量的可比性

    * 资本在不同时间不可比，需要进行价格调整

* 函数形式

  * 随机误差项
  * 变量间函数关系--线性与非线性关系

    * 线性关系说明完全可替代
    * 自变量为0，因变量依然有意义
    * 要素之间的替代性与替代弹性

      * 线性模型替代性无穷大

  * 
    常数项
    ------

* 估计

  * 变量之间独立

如何解释加了人口之后 变量不显著了

伪回归问题

Simple Linear Regression Model
------------------------------

Bayesian Methods
================

http://mindhacks.cn/2008/09/21/the-magical-bayesian-method/

https://docs.pymc.io/learn.html

Chapter 1 The Philosophy of Bayesian Inference
----------------------------------------------

Bayesian inference differs from more traditional statistical inference by preserving *uncertainty*. 

 *long-term frequency*  

Difference between frequentist and Bayesian


* frequentist inference function would return a number, Bayesian function would return *probabilities*
* Tools is still powerful and fast. Bayesian methods complement these techniques by solving problems that these approaches cannot, or by illuminating the underlying system with more flexible modelling.

$$
\begin{aligned}
P(A \mid X)=& \frac{P(X \mid A) P(A)}{P(X)} \
& \propto P(X \mid A) P(A) \quad(\propto \text { is proportional to })
\end{aligned} \
P(A):prior probabilitie \
P(A|X) : an updated posterior probabilities
$$

Example
^^^^^^^

Probability Distributions
^^^^^^^^^^^^^^^^^^^^^^^^^

Probabilistic programming
^^^^^^^^^^^^^^^^^^^^^^^^^
