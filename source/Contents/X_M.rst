.. role:: raw-html-m2r(raw)
   :format: html


Urban System Theory
===================

Urban scaling law
-----------------

About British cities – prior to the industrial revolution, Britain had one big city – London and a plausible hypothesis but we can’t test it because of lack of data, is that then british cities followed a rank size rule. But the cities of the industrial revolution were not formed from a central place theory (which is consistent with Zipf); they were built on the coalfield which is where all the northern cities are. The midlands was built also on coal and iron while Liverpool (as well as Bristol) where the ports. Basically our problems with validating Zipf, scaling size and so on in Britain (England) have something to do with historial development – history matters – or as we say in complexity theory, the evolution of the city system is path dependent

Fabulous question Zhengzi! This is another limitation of this type of analysis, it does not take into account the interaction between cities. But of course it matters, since this is linked to growth and spillovers, so the task is to find the impact, and this is still a research question!

There are really three types if scaling at least 1) inverse power laws that relate to size distributions like cities – Zipf –  2) scaling power laws that relate one variable to another – say income as a function of population – allometry – but there is a third – that we haven’t talked about today that is really important and central to spatial interaction – gravity transport models – the inverse square law that relates to what you are saying I think and we will look at this in urban simulation

Geography Information Science
=============================

Spatial Patterns and Spatial Autocorrelation
--------------------------------------------


* The importance of pattern
* Patterns of categorical point data – Point Pattern Analysis

  * Quadrat Analysis
  * Ripley's K
  * DBSCAN

* Patterns of spatially referenced continuous observations

  * Spatial autocorrelation
  * Defining near and distant things
  * Measuring spatial autocorrelation

    * Moran's I
    * LISA

The importance of pattern
^^^^^^^^^^^^^^^^^^^^^^^^^

Discrete Objects: Point Pattern Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*John Snow* : Broad street pump

Quadrat Analysis
~~~~~~~~~~~~~~~~

Ripley's K
~~~~~~~~~~

DBSCAN
~~~~~~

`Landscapetoolbox <https://wiki.landscapetoolbox.org/doku.php/spatial_analysis_methods:home>`_

Continuous Objects:
^^^^^^^^^^^^^^^^^^^

Spatial autocorrelation
~~~~~~~~~~~~~~~~~~~~~~~

`GeoDa <https://geodacenter.github.io/documentation.html>`_

Defining near and distant things
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Measuring spatial autocorrelation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Moran's I
"""""""""

LISA
""""

ggplot 2 seminar
~~~~~~~~~~~~~~~~

https://binchi1990.github.io/CASA_seminar2/challenges.html##challenge-1-reorder-the-items-in-legend

Quantitative Methods
====================

An Introduction to Quantitative Thinking
----------------------------------------


#. Understand the structure and focus of the module.
#. Consider the different roles of quantitative methods and their relevance in your work.
#. Develop a method for tackling quantitative problems.
#. Consider how to formulate a research question and structure a piece of quantitative writing.


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201107210923020.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201107210923020.png
   :alt: 


Fermi Estimation Problems
^^^^^^^^^^^^^^^^^^^^^^^^^

A process for tackling questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. State Assumptions.
#. Establish what you know (facts, formulae etc).
#. Establish what you don't know, but need to know.
#. Sort out 3 by estimating, calculating or researching.
#. Put all back together to get an answer.
#. Think about whether your answer is sensible. Verify if possible.

Good practice of a quantitative essay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Introduction
~~~~~~~~~~~~


* 
  Gives the reader a feel for your investigation.

* 
  Begins to justify your investigation


.. image:: http://www.zzzhou.me/images/2020/11/10/clip_image001.png
   :target: http://www.zzzhou.me/images/2020/11/10/clip_image001.png
   :alt: 


Literature Review
~~~~~~~~~~~~~~~~~


* Sources for context vs. sources for methods
* Is all the literature relevant to your investigation?
* How has your reading informed your methodology?
* Demonstrates the importance of your investigation
* Takes a critical perspective 
* (Engaging narrative)
* don't cite wikipedia


.. image:: http://www.zzzhou.me/images/2020/11/10/clip_image002.png
   :target: http://www.zzzhou.me/images/2020/11/10/clip_image002.png
   :alt: 


Research question
~~~~~~~~~~~~~~~~~


* explicit
* precise

  * real world relevance
  * informed by literature review
  * possibly split into sub-questions

Presentation of data
~~~~~~~~~~~~~~~~~~~~


* explains and visualize your data for the reader

Methodology
~~~~~~~~~~~


* Precise
* Reproducible
* Explicitly informed by literature review
* Explicitly designed to answer research question


.. image:: http://www.zzzhou.me/images/2020/11/10/clip_image003.png
   :target: http://www.zzzhou.me/images/2020/11/10/clip_image003.png
   :alt: 


Results
~~~~~~~


* Clear
* Complete
* Minimal Text
* Presented in most informative way possible

Discussion
~~~~~~~~~~


* Highlights key points from results
* Interprets and synthesises
* Acknowledges limitations
* Relates back to research question

Conclusion
~~~~~~~~~~


* Explicitly answers research question (as far as possible)
* Proposes further research


.. image:: http://www.zzzhou.me/images/2020/11/10/clip_image004.png
   :target: http://www.zzzhou.me/images/2020/11/10/clip_image004.png
   :alt: 


Overall Style
~~~~~~~~~~~~~


* Impersonal
  Use "we" or the passive ("A simulation was run.")
  Never use "I"
* 
  Not narrative
  Your Goal -- Communicate your results
  Not your goal -- Describe your every thought and action in chronological order

* 
  OBJECTIVES


  #. Understand the structure and focus of the course.
  #. Consider the different roles of quantitative methods and their relevance in your work.
  #. Develop a method for tackling quantitative problems.
  #. Consider how to formulate a research question and structure a piece of quantitative writing.

A Good Research Question...
^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ... cannot be answered with a single calculation ;
* ... is not vague ; (it could be quite long to include detail precision)
* ... asks about the real world, not just about data or methods.
* ... is interesting and valuable.
* ... is ambitious.

Lecture 1 -- Assignment
^^^^^^^^^^^^^^^^^^^^^^^

Read one of the example QM Projects* provided on Moodle. With reference to the mark scheme for written work, consider what mark you would award to the project in the streams 'Context and Review' and Communication'. Come to the next lecture prepared to talk about your chosen mark and why you have awarded it. (You may not understand the techniques used, but do not worry about this. Focus on the structure and the way that literature is used to support the work.)

Approaching & Communicating Data
--------------------------------

Objectives
^^^^^^^^^^


#. Understand basic data types 4中数据类型
#. Consider how to summarise and represent data. 数据描述方式
#. Understand basic distributions of data. 4种分布
#. Recognise three types of relationship between data series 三种关系

Assignment Discussion
^^^^^^^^^^^^^^^^^^^^^

Data types
^^^^^^^^^^

Source : `Level of measurement <https://en.wikipedia.org/wiki/Level_of_measurement>`_


* 有序变量可用均值？间隔变量可用均值？
* 2020年是1010年的两倍 年在做标志和做度量的区别


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201108104339605.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201108104339605.png
   :alt: 


Nominal data 名义变量
~~~~~~~~~~~~~~~~~~~~~


* Differentiates items based only on names； No order；Also called categorical data
* Example:

  * names, gender, country names
  * 土地利用分类数据

* Descriptive methods

  * Equality: 'apple' is not 'pear', 'apple' is 'apple'
  * Mode (the most common item)

Ordinal data 有序变量
~~~~~~~~~~~~~~~~~~~~~


* Allow for rank order, but not the relative degree of difference
* Example

  * measurement of opinions
  * 高中低程度

* Descriptive methods

  * Equality Mode
  * The median: middle-ranked item
  * Differences do not make sense, nor do means.

Interval data 间隔变量
~~~~~~~~~~~~~~~~~~~~~~


* Allow for the degree of difference between items, but not the ratio between them. The zero value is arbitrary.
* Example

  * temperature with the Celsius scale
  * 日期

* Descriptive methods

  * Equality, mode, median
  * Addition, Arithmetic mean
  * Ratio? The coordinate of 8 is twice as far as that of 4

    * 不能说20度是10度的两倍热

Ratio data 比率变量
~~~~~~~~~~~~~~~~~~~


* Allow for ratio between items; The zero value is unique and non-arbitrary.
* Example

  * mass, length, energy

* Descriptive methods

  * Equality, mode, median, arithmetic mean
  * Ratio

Descriptive statistics
^^^^^^^^^^^^^^^^^^^^^^

Mean median and mode
~~~~~~~~~~~~~~~~~~~~

https://statisticsbyjim.com/basics/measures-central-tendency-mean-median-mode/


* Outliers and skewed data have a smaller effect on the median

  * **When to use the median**\ :
    `Skewed <https://statisticsbyjim.com/glossary/skewed-data/>`_
    distribution, Continuous data, `Ordinal data <https://statisticsbyjim.com/glossary/ordinal-variables/>`_
  * **When to use the mode**\ :
    `Categorical data <https://statisticsbyjim.com/glossary/categorical-variables/>`_\ ,
    Ordinal data, Count data, Probability Distributions

* 对于正态分布，三者无差异；偏态分布，中位数较好；有序数据，中位数或者众数较好；众数可以通过密度分布计算

About DP and SF
~~~~~~~~~~~~~~~

• DP: decimal places 
• SF: significant figures

Variance and std: Quantifying Spread
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sample and Population
"""""""""""""""""""""

https://online.stat.psu.edu/stat200/book/export/html/21

.. image:: https://online.stat.psu.edu/stat200/sites/stat200/files/inline-images/InferenceGraphicSU17.png
   :target: https://online.stat.psu.edu/stat200/sites/stat200/files/inline-images/InferenceGraphicSU17.png
   :alt: 


Bessel's Correction
"""""""""""""""""""


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201108083413348.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201108083413348.png
   :alt: 



* 样本： n-1
* 全集： n

Visualizing data
^^^^^^^^^^^^^^^^

Outliers
~~~~~~~~


* Tukey Fences

$$
IQR = UQ-LQ 
LQ - 1.5\times IQR,UQ+1.5\times IQR
$$

Boxplot
~~~~~~~

.. code-block:: python

   ## This program creates a boxplot from data stored in a csv file and saves it as a png image.

   ## The data file must be one column of numbers - no column labels, etc.
   ## It must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
   ## It must be saved in the same folder as this program.
   ## See the file sample_boxplot_data.csv for reference.

   ## In the next line, replace sample_boxplot_data.csv with the filename of your data:
   data_filename = 'sample_boxplot_data.csv'

   ## In the next line, replace boxplot with the filename you wish to save as:
   output_filename = 'boxplot.png'

   ## Use the next line to set figure height and width (experiment to check the scale):
   figure_width, figure_height = 4,10

   ## You can ignore these two lines:
   import matplotlib.pyplot as plt
   import numpy as np

   data = np.genfromtxt(data_filename)

   ## If there are errors importing the data, you can also copy the data in as a list.
   ## e.g. data = [1.95878982, 2.59203983, 1.22704688, ...]

   ## This line creates the figure. 
   plt.figure(figsize=(figure_width,figure_height))

   ## Uncomment the next three lines to set the axis limits (otherwise they will be set automatically):
   ##axis_min = 0.95
   ##axis_max = 4.05
   ##plt.ylim([axis_min,axis_max])

   ## The next lines create and save the plot:
   plt.xlim([0.75,1.25])
   plt.xticks([])
   plt.boxplot(data, manage_ticks=(False))
   plt.savefig(output_filename)

Distributions
^^^^^^^^^^^^^


* mean,median,mode 和 boxplot 是对于数据的通用方法，简单方法
* 另一种描述数据的方法-- probability distribution Probability density  function
* 概率分布与直方图的区别？

  * 如果要描述样本，则使用经验分布（即直方图），如果要描述假设的基础分布，则使用pdf。
  * 概率质量函数（pmf）针对的是离散变量，例如泊松分布。
  * 大学课程 https://ocw.tudelft.nl/courses/observation-theory-estimating-unknown/

* 如何判断是否分布

  * 图形验证

    * 直方图
    * pdf
    * 经验累积概率图 : 也能拟合其他分布
    * 变换坐标轴的经验累积概率图
    * P-P图和Q-Q图

  * 统计检验

    * Kolmogorov-Smirnov检验
    * Anderson-Darling检验
    * Shapiro-Wilk检验

* https://docs.scipy.org/doc/scipy/reference/stats.html

Normal Distribution
~~~~~~~~~~~~~~~~~~~

Log-normal
~~~~~~~~~~


* 不可小于0 一些值非常大


.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/PDF-log_normal_distributions.svg/600px-PDF-log_normal_distributions.svg.png
   :target: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/PDF-log_normal_distributions.svg/600px-PDF-log_normal_distributions.svg.png
   :alt: 


Poisson
~~~~~~~


* Poisson Distribution gives the probability of k events.
* how many times things happen?
* 
  .. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Poisson_pmf.svg/650px-Poisson_pmf.svg.png
     :target: https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Poisson_pmf.svg/650px-Poisson_pmf.svg.png
     :alt: 

Exponential distribution
~~~~~~~~~~~~~~~~~~~~~~~~


* The Exponential distribution is linked to the Poisson distribution.
* If the Poisson measures the probability of x events within a time period, then the Exponential measures how long we are likely to wait between events.
* So imagine an emergency room in a hospital. The exponential distribution will tell us how likely we are to wait x amount of time from one patient arriving to the next.

:raw-html-m2r:`<u>Guessing Distribution</u>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. Shoe size normal
#. The thickness of tree bark lognormal
#. The number of times a website is accessed per minute. poisson
#. The time between phone calls at a call centre. exponential
#. The number of popcorn kernels popping in a 5 second window
   **normal** ？？ poisson

   * 这是个时间序列而不是单位时间发生的次数

https://www.youtube.com/watch?v=YmOsDTczOFs&ab_channel=MindYourDecisions

Boxcox transform方法
~~~~~~~~~~~~~~~~~~~~


* 只是一种将数据转换为正态分布的方法
* 改变了数据的意义

Relationships
^^^^^^^^^^^^^


* 三种关系
* 如何判断关系

  * using logarithms to straighten curves
  * If your data makes a straight line on a log-linear plot, it may be an exponential relationship
  * If your data makes a straight line on a log-log plot, it may be an power law relationship
  * 如果数据在y对数图上是一条直线，那么它可能是指数关系
  * 双对数图上-- 幂律

* zipf's law

Linear
~~~~~~

Bus stops in a line road and in a spatial circle

Kleiber's Law and power law
~~~~~~~~~~~~~~~~~~~~~~~~~~~

$$
Metabolic rate = M \times x^{n} \
x: body mass\
n: power
$$
Power law


* for Cities
* Linear relationships are power laws!
* 对于幂律，这种关系可能只适用于超过一定大小的值。考虑忽略小的价值
* 对于时间数据(例如年份)，可能没有自然的"零"。考虑从一个合理的基准时间度量。(例如，如果数据始于1900年，使用"自1900年以来的年份")
* kleiber's law都是power law 的特殊
* zipf's law

Exponentials
~~~~~~~~~~~~

..

   " The greatest shortcoming of the human race is our inability to understand the exponential function

   ​                                                                                                                                                         -- Albert Bartlett


----

:raw-html-m2r:`<u>Suggested Reading/Viewing</u>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* lectures
* `Padlet for disscussion qm projects <https://padlet.com/hannahfry/bbua7lcjtkyq6mh4>`_
* `Logarithms from Khan Academy <https://www.khanacademy.org/math/algebra2-2018/exponential-and-logarithmic-functions/introduction-to-logarithms/v/logarithms>`_
* Assignments

----

Basic Mathematical Catch-Up


* Introduction to logarithms: http://www.purplemath.com/modules/logs.htm
* A straightforward discussion of variance and standard deviation: averages, their advantages and disadvantages: 
* Box plots: http://www.physics.csbsju.edu/stats/box2.html

Variance - Deeper Thinking


* For those who know a bit of stats and have read that the sample variance should use n-1 as a divisor:
  http://www.crataegus.me.uk/thoughts/bessel_correction.html

Excel Tutorial


* For those not comfortable with Excel, here is a short entry-level tutorial on using Excel formulae:
  http://www.excel-easy.com/introduction/formulas-functions.html
* That site has loads more Excel advice, so have a look around there if you like.

Power Laws


* A TED talk on power laws for cities, given by one of the authors of the paper that I referred to in the lecture. Entertaining, relevant and informative and only 17 minutes long: https://www.ted.com/talks/geoffrey_west_the_surprising_math_of_cities_and_corporations\##t-173864
* Here is a nice tutorial on power laws and log-log plots from the University of Plymouth. It goes into a little more detail than we did, so it is good for people who had trouble following (skip the bits that don't relate to what was covered in the lecture) or who are confident and want to extend/test their knowledge.http://www.reading.ac.uk/AcaDepts/sp/PPLATO/imp/interactive%20mathematics/loglog2.pdf
* Here is an academic paper on power laws in cities. It is well worth a read for background knowledge, but do not worry if you do not understand all of it (skip the mathematical section: "Urban Growth Equation" on p7304, unless you are a mathematician or a masochist). http://www.pnas.org/content/104/17/7301.full.pdf
* There is also an accessible summary of the paper here:http://scienceblogs.com/purepedantry/2007/10/18/power-laws-and-cities/
* But note that there is a mistake in that summary. When they talk about "exponential" increases, they mean "superlinear". The academic paper does not discuss any exponential relationships.

----

Distributions

**Light Accessible Reading/Viewing**

Zipf's Law:


* https://plus.maths.org/content/mystery-zipf
* http://io9.com/the-mysterious-law-that-governs-the-size-of-your-city-1479244159
  Video: https://youtu.be/fCn8zs912OE?t=4

**Tutorials**
Poisson Distribution (Good accessible overview):
https://www.umass.edu/wsp/resources/poisson/
Stat Trek on Distributions:
http://stattrek.com/probability-distributions/probability-distribution.aspx?Tutorial=Stat
Normal Distribution (In significant depth):
http://onlinestatbook.com/2/normal_distribution/intro.html

**More Technical Background**
Lognormal across the
sciences:http://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
Working with Power Laws:


* `http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pd <http://www-personal.umich.edu/~mejn/courses/2006/cmplxsys899/powerlaws.pdf>`_
* https://arxiv.org/pdf/0706.1062.pdf

**Further Academic Papers**
There is More than a Power Law in Zipf: http://www.nature.com/articles/srep00812

----

Albert Bartlett's lecture:https://youtu.be/O133ppiVnWY
BBC article on population projections: http://news.bbc.co.uk/1/hi/8000402.stm
Telegraph article on oil: http://www.telegraph.co.uk/news/earth/energy/oil/9867659/Why-the-world-isnt-running-out-of-oil.html

Assignment
^^^^^^^^^^


#. Watch Albert Bartlett's lecture on the exponential function: http://www.youtube.com/watch?v=F-QA2rkpBSY (You only need to watch the first 20 minutes or so.)
   Read the following articles:http://news.bbc.co.uk/1/hi/magazine/8000402.stm
   http://www.telegraph.co.uk/news/earth/energy/oil/9867659/Why-the-world-isnt-running-out-of-oil.html
   Consider what we should conclude about quantitative predictions?
#. Have a play with the excel data investigation. It will guide you through how to plot and explore data in Excel.
#. Look at the relationships data sets on moodle. What do they reveal about the underlying relationships?

Measuring Relationships
-----------------------

Objectives
^^^^^^^^^^


#. Understand the concept of covariance, correlation and what it says about data relationships. 
#. Be able to measure a data relationship using simple linear regression. 
#. Learn how regression can be extended for data with more than two dimensions. 
#. Understand how to identify whether additional data provides additional information.

Lectures
~~~~~~~~

How many ways do we have to measure correlation? What are the main differences between these measurements? What is partial correlation and how can we understand it intuitively?
We can't use correlation to predict, as correlation does not imply causation, but if variables are dependent then they are either causal to each other (in either direction) or driven by a common driver.
Do we need to perform a heteroskedasticity test before regression, and how can we do this?


* data type
* distribution
* relationship
* regression

Motivations for data transformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. To formulate a different question
#. To meet the assumptions of a statistical inference procedure
#. To make data easier to visualise

Outliers and Dealing with it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 先用方法识别outliers ，根据经验判断是否保留
* types of outliers

  #. Error
  #. Points not following the pattern

     * If you are studying the overall pattern, they need to be removed -- e.g. City of London (in London) -- e.g. Vantican City (1000 pop, gender ratio 7:1)
     * "Statistical oddities"

  #. Points that are essential to the overall pattern

     * Don't remove them e.g. New York in UＳ pop data

* There are many approaches to identify outliers (e.g. Tukey fences), but determining an outlier is a subjective exercise.
* Dealing with outliers (not sure type 2 or 3)

  * Retention, **but the application should use methods that are robust to outlier points**
  * Exclusion. If some outliers are excluded, the reasons should be clearly stated on the report.

----

Part 1. Covariance, Correlation, and Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variability
~~~~~~~~~~~

a single variable
"""""""""""""""""

Co-variability of two variables
"""""""""""""""""""""""""""""""

ANOVA (not covered here)
""""""""""""""""""""""""

• Whether two or more population means are equal • When there are only two populations, it is called two sample t-test (covered in Lecture 5) 
• E.g. is the mortality rate of Covid-19 the same across different cities?

Covariance
""""""""""

"Do the two variables change in the same direction?" "To what extent do they change together?"


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201020174858181.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201020174858181.png
   :alt: 



* Meaning
* Meaning of sign
* Range? -inf~inf
* Normalised?  no 
* Symmetric

Larger Variance  


.. image:: http://www.zzzhou.me/images/2020/11/12/image-20201112225329571.png
   :target: http://www.zzzhou.me/images/2020/11/12/image-20201112225329571.png
   :alt: image-20201112225329571


Correlation
~~~~~~~~~~~

Person Correlation
""""""""""""""""""

$$
cor(X,Y) = r(X,Y) = \frac{cov(X,Y)}{std(X)\times std(Y)}
$$

**limitations**


* The Pearson correlation coefficient measures only **linear association**\ : how nearly the data fall on a straight line.
* It is not a good summary of association if the scatterplot has a nonlinear (curved) pattern.
* When you present the correlation, remember to present a scatterplot.
* The Pearson correlation coefficient is appropriate only for interval or ratio variables, not nominal or ordinal variables -- even if their values are numerical.
* Note the difference between the data type of the variable and the value.


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201020174836667.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201020174836667.png
   :alt: image-20201020174836667


Spearman's Rank Correlation Coefficient
"""""""""""""""""""""""""""""""""""""""

$$
r\ *{s}=\rho*\ {\mathrm{rg}\ *{X}, \mathrm{rg}*\ {Y}}=\frac{\operatorname{cov}\left(\mathrm{rg}\ *{X}, \mathrm{rg}*\ {Y}\right)}{\sigma\ *{\mathrm{rg}*\ {X}} \sigma\ *{\mathrm{rg}*\ {Y}}}
$$


* It is applicable for interval/ratio data

  * Transform the value into ranks;
  * Calculate the Rank correlation.

* But it is different from Pearson's correlation, and they are
  incomparable.
* 
  Less sensitive to outliers than Pearson correlation


  .. image:: http://www.zzzhou.me/images/2020/11/10/image-20201020175750498.png
     :target: http://www.zzzhou.me/images/2020/11/10/image-20201020175750498.png
     :alt: 


Limitations
"""""""""""


* Pearson correlation is not applicable for nominal/ordinal data.
* It measures only linear association, and is not a good summary for non-linear data.
* It is a measure of association, not causation. It is not robust to outliers, less robust than Spearman's rank correlation.

correlation is a global metric, it doesn't give the local relation.

----

Part 2. Linear Regression
^^^^^^^^^^^^^^^^^^^^^^^^^


#. Where to place the line?
#. How well does the line represent the data?


.. image:: http://www.zzzhou.me/images/2020/11/10/image-20201020181527698.png
   :target: http://www.zzzhou.me/images/2020/11/10/image-20201020181527698.png
   :alt: 


Necessary Conditions
~~~~~~~~~~~~~~~~~~~~


* Linear relationship exists
* Independent errors : one error is not affected by the value of another error 
* Normally distributed errors : for each value of x, the errors have a normal distribution about the regression line.
* Equal error variance for all x values :  the error value does not change because of the x values

NOT a Necessary Condition! : Normally Distributed Data

verifying the conditions

residual independent 

normally distributed 

equal variance

Linear regression exists
~~~~~~~~~~~~~~~~~~~~~~~~

The relationship between y and x is linear; that is, there is an equation, y=mx+c+ε that constitutes the population model.

Independent errors
~~~~~~~~~~~~~~~~~~


* The residuals are independent; the value of one error is not affected by the value of another error.
* In probability, two events A and B are independent if knowing that B happens does not alter the probability that A happens. E.g. , flipping two coins.
* A and B are independent if Pr[B]=0 or Pr[A|B] = Pr[A]
* But... how can we know that?

Normally distributed errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~


* For each value of x, the errors have a normal distribution about the regression line. This normal distribution is centred on the regression line.
* It may be written as ε~𝑁(0, σ2)

Equal error variance for all x values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* The errors about the regression line do not vary with x; that is, V[ε|x] = σ2 residual plot

Part 3. Multiple Regression
^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. Can we combine greenery and natural light to create a model for predicting wellbeing?
#. How does the combined model compare with individual models?
#. Can we put categorical variables into the model?

Question 1
""""""""""

With R2 values of 30-40%, both models leave a lot of variation unaccounted for. Could we do better, by using BOTH data series to explain the variation in the reported well-being?

Readings
^^^^^^^^

Tools and Techniques
~~~~~~~~~~~~~~~~~~~~

**Covariance and Correlation:**\ http://ci.columbia.edu/ci/premba_test/c0331/s7/s7_5.html
**Spearman's Rank Correlation Coefficient:**\ https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php

*As an aside, while there are lots of Spearman's Rank information resources online, it is difficult to find one that does not make misleading claims about (surprise, surprise) normality assumptions. Many resources claim that you would use Spearman rather than Pearson correlation if you think your data series are not normally distributed.
This is false. Pearson correlation does not require normally distributed data (though some associated statistical tests do). The following two resources, for example, would also be good if it were not for such claims:*

http://www.statstutor.ac.uk/resources/uploaded/spearmans.pdf
http://www.biostathandbook.com/spearman.html

**Linear Regression - Tutorials**
Here is an excellent course on regression. I would recommend that you use it as your main reference work for this subject. Lessons 1, 3 and 4 are most relevant to simple linear regression:
https://onlinecourses.science.psu.edu/stat501/lesson/1
`https://onlinecourses.science.psu.edu/stat501/lesson/3 <https://onlinecourses.science.psu.edu/stat501/lesson/1>`_
`https://onlinecourses.science.psu.edu/stat501/lesson/4 <https://onlinecourses.science.psu.edu/stat501/lesson/1>`_

The course also goes through multiple linear regression (Lessons 5-7) and discusses the use of categorical variables in detail (Lesson 8):
`https://onlinecourses.science.psu.edu/stat501/lesson/5 <https://onlinecourses.science.psu.edu/stat501/lesson/1>`_
`https://onlinecourses.science.psu.edu/stat501/lesson/6 <https://onlinecourses.science.psu.edu/stat501/lesson/1>`_
`https://onlinecourses.science.psu.edu/stat501/lesson/ <https://onlinecourses.science.psu.edu/stat501/lesson/1>`_\ 7

Here is a lesson on performing simple and multiple linear regression in Python. It is a lot more advanced than the Python we have covered, but may be of interest for those who are fairly confident with the language:
http://www.dataschool.io/linear-regression-in-python/

Stat Trek (http://stattrek.com/) is another good site for learning about concepts in statistics. Here is the start of their material on regression: http://stattrek.com/regression/linear-regression.aspx?Tutorial=Stat

[However, note that Stat Trek say "For any given value of X... the Y values [must be] roughly normally distributed", which is true (this is effectively equivalent to saying that the residuals must be normally
distributed), but they then imply that looking at a histogram of the data would help to confirm this, which is of course false. The histogram might show that the DATA looks normally distributed, but as we now know,  this is irrelevant! It's a residuals vs fits plot you need.]

Research Skills
~~~~~~~~~~~~~~~

UCL Library's video series on using Web of Science to search for academic publications
https://youtu.be/AgTk3kA

Just for fun
~~~~~~~~~~~~

Spurious Correlations: http://www.tylervigen.com/spurious-correlations
The Great Horse Manure Crisis:http://www.historic-uk.com/HistoryUK/HistoryofBritain/Great-Horse-Manure-Crisis-of-1894/

Advanced Regression
-------------------


* 回归需不需要变量正态化？什么时候需要正态化，标准化

Assignment 1
------------

Hypothesis Testing
------------------

**1.**  State your hypotheses.

**2.**  State your significance level: 𝛂

**3.**  What is the evidence (E)? (The Test Statistic)

**4.**  Calculate the probability of seeing evidence at least  as extreme as E, *if* H0 *is true*. (The “p-value”)

**5.** If the p-value is smaller than the significance, reject  H0 and accept H1. Otherwise there is not enough  evidence to reject H0.


.. image:: http://www.zzzhou.me/images/2020/11/17/image-20201117181037540.png
   :target: http://www.zzzhou.me/images/2020/11/17/image-20201117181037540.png
   :alt: image-20201117181037540


Chi squared 开 threshold

what chance of getting these observed values?

Quiz


#. 
#. two 
#. a firm discrimination between 


* 

Cluster Analysis
----------------

Part 1: Hypothesis testing recap
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, the first question is whether your INDEPENDENT variable is categorical or quantitative. The second is whether your DEPENDENT variable categorical or quantitative.

0.01 0.05 p value 

Part 2: Cluster analysis – why should I care?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sorry, I am always get confused about the difference among Boxcox transformation, log transformation, z-scores and  standardisation, it seems that all of these are transforming things on the same scale, how to choose the proper method?

Sorry, I am always confused about the difference between Boxcox transformation, log transformation, z-scores, and standardization. It seems that all of these are transforming things on the same scale. How to choose the proper method?

Will the converted data lose some features

Part 3: Before you start
^^^^^^^^^^^^^^^^^^^^^^^^

如何比较谁更异常？

标准化不会损失特征

Part 5: Hierarchical clustering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Part 6: How good are your clusters?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Part 7: Some tips and tricks for your written work
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Optimising Limited Resources
----------------------------

Modelling the World
-------------------

Statistical Traps & Advanced Topics
-----------------------------------

wk4
---


* VIF for multicollinearity

Introduction to Programming
===========================

Reading week
------------

In addition to looking for relevant content in [@dignazio:2020] (\ `URL <https://bookbook.pubpub.org/data-feminism>`_\ ), you will also want to check consider:

Dignazio:2020
^^^^^^^^^^^^^

Elwood:2017
^^^^^^^^^^^

Elwood:2018
^^^^^^^^^^^

Crawford : 2015 `DOI <https://doi.org/10.1007/s10708-014-9597-z>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ontological, epistemological, and ethical challenges that arise when social media datasets are used to understand crisis events
* 


* [@Elwood:2017] `DOI <https://doi.org/10.1080/13658816.2017.1334892>`_
* [@Elwood:2018] `DOI <https://doi.org/10.1080/0966369X.2018.1465396>`_
* [@Bemt:2018] `DOI <https://doi.org/10.1080/03098265.2018.1436534>`_
* [@Amoore:2019] `DOI <https://doi.org/10.1177%2F0263276419851846>`_

Week 6：Spatial Data
--------------------

Lectures
^^^^^^^^

Mapping
~~~~~~~


* Purely Computational vs. Mostly Computational

  * Wider variety of output formats (e.g. Atlases, 3D/web).
  * Better support for 'finishing touches' (e.g. scalebars, north arrows, rule-based labels, etc.).
  * Better-quality output for less effort (e.g. Model Builder + QGIS styles).

* 
  Every Building in America


  * `Building footprints <https://github.com/Microsoft/USBuildingFootprints/>`_ collected by Microsoft, but presentation by New York Times `highlights society-nature interactions <https://www.nytimes.com/interactive/2018/10/12/us/map-of-every-building-in-the-united-states.html>`_.
  * 
    .. image:: http://www.zzzhou.me/images/2020/11/17/NYT-MS-History.png
       :target: http://www.zzzhou.me/images/2020/11/17/NYT-MS-History.png
       :alt: NYT-MS-History

* 
  A Deceptively Simple Problem

..

      We want to show data on a map in a way that is **both accurate and informative**.



* Classification

  * The greater the accuracy of a **choropleth** or other class-based map, the less it’s possible generalise from it.
  * There is no 'right' way to group data into an arbitrary number of discrete classes (a.k.a. to generalise).

* Different ways of representation will be totally different

  * Judgement should based on distribution
  * Six Views of Employment

..

   ..

      Different colour and break schemes not only give us different **views** of the data, they give us different **understandings** of the data! Each potentially changes how the data looks and, consequently, how we perceive the distribution.



* Maps have a 'Rhetoric' `Do maps lie? <https://www.youtube.com/watch?v=G0_MBrJnRq0>`_ it always helps to look at a map with a critical  eye.

Exploratory Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~


* Epicyclic Feedback

.. list-table::
   :header-rows: 1

   * - 
     - Set Expectations
     - Collect Information
     - Revise Expectations
   * - Question
     - Question is of interest to audience
     - Literature search/experts
     - Sharpen question
   * - EDA
     - Data are appropriate for question
     - Make exploratory plots
     - Refine question or collect more data
   * - Modelling
     - Primary model answers question
     - Fit secondary models / analysis
     - Revise model to include more predictors
   * - Interpretation
     - Interpretation provides specific and meaningful answer
     - Interpret analyses with focus on effect and uncertainty
     - Revise EDA and/or models to provide more specific answers
   * - Communication
     - Process & results are complete and meaningful
     - **Seek feedback**
     - Revises anlyses or approach to presentation



* 
  Approaching EDA


  * From: `EDA—Don't ask how, ask what <https://medium.com/towards-artificial-intelligence/exploratory-data-analysis-eda-dont-ask-how-ask-what-2e29703fb24a>`_\ :
  * Descriptive Statistics: get a high-level understanding of your dataset
  * Missing values: come to terms with how bad your dataset is
  * Distributions and Outliers: and why countries that insist on using different units make our jobs so much harder
  * Correlations: and why sometimes even the most obvious patterns still require some investigating

    * Preview data
    * Check total number of entries and column types
    * Check any null values
    * Check duplicate entries
    * Plot distribution of numeric data (univariate and pairwise joint distribution)
    * Plot count distribution of categorical data
    * Analyse time series of numeric data by daily, monthly and yearly frequencies

* 
  Signal & Noise  


  * Starting at a chart 

    * The problem of relying on statistics alone was amply illustrated by Anscombe's Quartet (1973)...
    * We *are not* very good at looking at spreadsheets. 
    * We *are* very good at spotting patterns visually.
    * ^ Or, as Albert Einstein reportedly said: "If I can't picture it, I can't understand it."

  * What Makes a Good Plot?

    * Serves a **purpose** — it is clear how it advances the argument in a way that could not be done in the text *alone*.
    * Contains only what is **relevant** — zeroes in on what the reader *needs* and is not needlessly cluttered.
    * Uses precision that is **meaningful** — 
    * Far too many charts or tables could be easily written up in a single sentence.
    * Far too many charts or tables contain redundancy, clutter, and 'flair'.\
    * Don't report average height of your class to sub-millimeter level accuracy, or lat/long to sub-atomic scale.

  * The Purpose of a Chart

    * Think of a chart or table as part of your ‘argument’ – if you can’t tell me how a figure advances your argument (or if your explanation is more concise than the figure) then you probably don’t need it.
    * Identify & prioritise the relationships in the data.
    * Choose a chart type/chart symbology that gives emphasis to the most important relationships.

  * Beyond the Chart
  * Why a table is sometimes better than a chart:

    * You need to present data values with greater detail
    * You need to enable readers to draw comparisons between data values
    * You need to present the same data in multiple ways (\ *e.g.* raw number *and* percentage)
    * You want to show many dimensions for a small number of observations
    * 表格的格式  数字对齐方式 信息不重复 不遗漏

Links


* `Pandas Reference <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html>`_
* `A Guide to EDA in Python <https://levelup.gitconnected.com/cozy-up-with-your-data-6aedfb651172>`_ (Looks very promising)
* `EDA with Pandas on Kaggle <https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas>`_
* `EDA Visualisation using Pandas <https://towardsdatascience.com/exploratory-data-analysis-eda-visualization-using-pandas-ca5a04271607>`_
* `Python EDA Analysis Tutorial <https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python>`_
* `Better EDA with Pandas Profiling <https://towardsdatascience.com/a-better-eda-with-pandas-profiling-e842a00e1136>`_ **[Requires module installation]**
* `EDA: DataPrep.eda vs Pandas-Profiling <https://towardsdatascience.com/exploratory-data-analysis-dataprep-eda-vs-pandas-profiling-7137683fe47f>`_ **[Requires module installation]**
* `A Data Science Project for Beginners (EDA) <https://medium.com/analytics-vidhya/a-data-science-project-for-beginners-exploratory-data-analysis-eda-d334f58f94ee>`_
* `EDA: A Pracitcal Guide and Template for Structured Data <https://towardsdatascience.com/exploratory-data-analysis-eda-a-practical-guide-and-template-for-structured-data-abfbf3ee3bd9>`_
* `EDA—Don't ask how, ask what <https://medium.com/towards-artificial-intelligence/exploratory-data-analysis-eda-dont-ask-how-ask-what-2e29703fb24a>`_ (Part 1)
* `Preparing your Dataset for Modeling – Quickly and Easily <https://medium.com/towards-artificial-intelligence/preparing-your-dataset-for-modeling-quickly-and-easily-c8c1b89fdb2e>`_ (Part 2)
* `Handling Missing Data <https://towardsdatascience.com/handling-missing-data-for-a-beginner-6d6f5ea53436>`_
* `Introduction to Exploratory Data Analysis (EDA) <https://medium.com/code-heroku/introduction-to-exploratory-data-analysis-eda-c0257f888676>`_

Exploratory Spatial Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* PySAL

{{Mind-Map}}
PySAL
    libpysal
        weights
            Distance Weights
            Continguity Weights
    explore
        esda
        inequality
        pointpats
        ...
    model
        mgwr
        spglm
        spreg
        ...
    viz
        legendgram
        mapclassify
        splot


* `EDA with Pandas on Kaggle <https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas>`_
* `EDA Visualisation using Pandas <https://towardsdatascience.com/exploratory-data-analysis-eda-visualization-using-pandas-ca5a04271607>`_
* `Python EDA Analysis Tutorial <https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python>`_
* `Better EDA with Pandas Profiling <https://towardsdatascience.com/a-better-eda-with-pandas-profiling-e842a00e1136>`_ **[Requires module installation]**
* `Visualising Missing Data <https://geopandas.org/mapping.html##missing-data>`_
* `Choosing Map Colours <https://geopandas.org/mapping.html##choosing-colors>`_

Readings
^^^^^^^^

Dignazio 2020
~~~~~~~~~~~~~

[@dignazio:2020, chap. 6] **The Numbers Don't Speak for Themselves** in *Data Feminism*\ ; `Pre-review URL <https://bookbook.pubpub.org/pub/6ui5n4vo>`_

Elwood 2017
~~~~~~~~~~~

[@Elwood:2017] `DOI <https://doi.org/10.1080/13658816.2017.1334892>`_

Practical
^^^^^^^^^


* ``isna`` and ``isnull``  : 完全相同
* ``pdf[pdf.id.isna()].index.values`` ： 查找空值
* ``pdf.longitude`` and ``pdf["longitude"]`` ：似乎也没差别

Assessment ##2
--------------

..

   I had interpreted it as doing the biography on just the August listing dataset we were given and then in the questions like ‘to what extent is the data complete’ I analysed whether this dataset in isolation was a complete picture of the process it claims for us to examine and whether integration of the other datasets would be more beneficial (i.e. time-series analysis for airbnb impact etc)



* The focus here is really on approaching the ‘assigned’ data with a critical eye—what are the strengths and weaknesses, what are the ethics, etc. Link it to the readings. While it is not necessary to have run any code/done any analysis, it will undoubtedly be easier for many of you to ground your thinking in concrete examples drawn from the data. Bringing other data sets from the InsideAirbnb site into it may help but might just confuse.
* It is not necessary that you perform any new work in Python for Assessment 2. If you are having trouble making *sense* of the data and feel that it would help to think more 'concretely' then you might want to revisit the summary information and plots that we did for one or more of the columns we’ve not looked at... but that is *only* if you think it will help you to answer the questions in greater detail and with more specificity. I am not asking for you to do anything more with the code than you have already done. You will not get a better mark for having written more/new code.
* The readings have invited you to think about how data is generated, for what purpose(s), who is included/excluded, what is missing, etc., as well as issues of ethics (such as the ethical use of data), and these questions and topics are intended to support a critical engagement with the data. I would start by reading up on how the data was collected and for what purpose, and then use that as a launching point for the rest of the assessment.
* It is not necessary that you look at the other data available on the InsideAirbnb web site but, again, if it helps you think through the issues in greater detail then you are free to reference them in your answer. You will not get a better mark for discussing other data sets in detail.
* Please use the template to answer the questions, you don't need to write an intro/conclusion/etc. By the time you've finished filling in the Markdown template you'll have something fairly well-organised that can, hopefully, be read as a kind of highly-structured essay.

Week 7 : Textual Data
---------------------

Lectures
^^^^^^^^

Notebook as Documents
~~~~~~~~~~~~~~~~~~~~~

Not Just for Code
"""""""""""""""""

..

   Markdown and Notebooks can be used for a lot more than just code! In conjunction with Pandoc and/or LaTeX they become platforms for publication.


Recall: Tangled Workflows
"""""""""""""""""""""""""

It's not *just* about mixing code and comment, we *also* want:


* To separate *content* from *presentation*
* To define *mappings* between presentation styles
* To produce the *best-quality* output for the format chosen


.. image:: http://www.zzzhou.me/images/2020/11/25/126z19ld.jpg
   :target: http://www.zzzhou.me/images/2020/11/25/126z19ld.jpg
   :alt: 


^ Examples of this include CSS for web sites, LaTeX templates, and Markdown styles.
^ `MVC approach <https://hackernoon.com/beginners-guide-to-ruby-on-rails-mvc-model-view-controller-pattern-4z19196a>`_ to software design.

Pandoc
""""""

Tool for converting documents *between* formats, including:


* Plain Text/YAML
* Markdown
* LaTeX/PDF
* HTML/Reveal.js
* Jupyter Notebook
* XML/ODT/DOCX
* EPUB/DocBook
* BibTeX/JSON

LaTeX
"""""

Intended for `type-setting of scientific documents <https://www.latex-project.org/about/>`_\ , but has been used for slides, posters, CVs, etc. It is *not* a word processor, it's more like a *compiler*.


.. image:: http://www.zzzhou.me/images/2020/11/25/LaTeX-1.png
   :target: http://www.zzzhou.me/images/2020/11/25/LaTeX-1.png
   :alt: LaTeX-1



.. image:: http://www.zzzhou.me/images/2020/11/25/LaTeX-2.png
   :target: http://www.zzzhou.me/images/2020/11/25/LaTeX-2.png
   :alt: LaTeX-2


^ This format is based on Edward Tufte's VSQD and can be found onHub](https://tufte-latex.github.io/tufte-latex/).

LaTeX in Practice
#################

You  write LaTeX in any text editor, but specialist apps like `Texpad <https://www.texpad.com/>`_ or `Overleaf <https://www.overleaf.com/>`_ make it easier.

.. code-block:: latex

   \documentclass[11pt,article,oneside]{memoir}
   \newcommand{\bl}{\textsc{bl}~\/}
   \usepackage{tabularx}

   \begin{document}
   \maketitle 

   This report provides an overview of activities ...

   \section{Applications}
   A primary objective was the submission...

^ UCL has an institutional license for Overleaf. 
^ This document is then *compiled* (or 'typeset') with the commands provided by the preamble being interpreted and applied. Depending on the length of the document and sophistication of the styles it can take up to 3 or 4 minutes for a book-length document, but small documents should compile in a few seconds.

^ Compilation allows us to do things like have Master Documents that actually work, include PDFs, make forwards and backwards references.

BibTeX
######

Provides bilbiographic support for LaTeX but widely used by other utilities as is *also* plain-text.

.. code-block:: bibtex

   @article{Lavin:2019,
           Author = {Lavin, Matthew J.},
           Doi = {10.46430/phen0082},
           Journal = {The Programming Historian},
           Number = {8},
           Title = {Analyzing Documents with TF-IDF},
           Year = {2019},
           Bdsk-Url-1 = {https://doi.org/10.46430/phen0082}}

   @incollection{Kitchin:2016,
           Author = {Kitchin, R. and Lauriault, T.P. and McArdie, G.},
           Booktitle = {Smart Urbanism},
           Chapter = {2},
           Editor = {Marvin, Luque-Ayala, McFarlane},
           Title = {Smart Cities and the Politics of Urban Data},
           Year = {2016}}

BibTeX in Practice
##################

To reference a document we then need to tell LaTeX or Pandoc where to look:

.. code-block:: latex

   \bibliographystyle{apacite} ## LaTeX
   \bibliography{Spatial_Data_Chapter.bib} ## LaTeX

With citations following formats like:

.. code-block:: latex

   \citep[p.22]{Reades2018} ## LaTeX

Or: 

.. code-block:: markdown

   [@dignazio:2020, chap. 4] ## Markdown

Reveal.js
#########

JavaScript-based presentation framework. Can use Markdown (using the separator ``---`` to separate slides) to generate portable interactive slides including references/bibliographies.

Compare:


* https://github.com/darribas/wmn/blob/master/src/slides/lecture_01.md
* https://github.com/darribas/wmn/blob/master/src/slidedecks/lecture_01.html
* http://darribas.org/wmn/slidedecks/lecture_01.html##/

From Markdown...
################

.. code-block:: bash

   pandoc Syllabus.md \
     -H ./bib/head.tex \
     -H ./bib/chapter.tex \
     -H ./bib/refs.tex \
     -V documentclass=memoir \
     --pdf-engine=xelatex \
     --filter=pandoc-citeproc \
     --metadata-file=metadata.yml \
     --highlight-style=pygments \
     -o Syllabus.pdf

To PDF!
#######


.. image:: http://www.zzzhou.me/images/2020/11/25/Syllabus.png
   :target: http://www.zzzhou.me/images/2020/11/25/Syllabus.png
   :alt: Syllabus


Pros
####


* Simplicity (while writing)
* Flexibility of Form
* Version Control
* High-Quality Outputs
* Enforced Structure

Cons
####


* Complexity (when formatting)
* Collaboration (can be harder)

^ If your document lacks structure (headings, sub-headings, etc.) then it's *impossible* to get a good-looking document. 

^ Conversely, *because* LaTeX and Markdown force you to add structure they ensure that things like ToCs, ToFs, and Bibliographies will generally work 'as advertised'.

Recap of Formatting
"""""""""""""""""""

Headings
########

.. list-table::
   :header-rows: 1

   * - Markdown
     - LaTeX
   * - ``## Heading Level 1``
     - ``\section{Heading Level 1}``
   * - ``### Heading Level 2``
     - ``\subsection{Heading Level 2}``
   * - ``#### Heading Level 3``
     - ``\subsubsection{Heading Level 3}``


Inline Elements
###############

.. list-table::
   :header-rows: 1

   * - Markdown
     - LaTeX
   * - ``1. Numbered item 1``
     - ``\begin{enumerate} \n \item ... \end{enumerate}``
   * - ``- Bulleted list item 1``
     - ``\begin{itemize} \n \item ... \n \end{itemize}``
   * - ``_italics_`` or ``*italics*``
     - ``\emph{italics}`` or ``\textit{italics}``
   * - ``**bold**``
     - ``\textbf{bold}``
   * - ``> blockquote``
     - ``\begin{quote} \n blockquote \end{quote}``
   * - ``Some `code` is here``
     - ``Some \texttt{code} is here``
   * - ``[Link Text](URL)``
     - ``\href{Link Text}{URL}``
   * - ``![Alt Text](Image URL)``
     - ``\begin{figure}\n \includegraphics[opts]{...}\n \end{figure}``


Mathematics
###########

.. list-table::
   :header-rows: 1

   * - Markdown
     - LaTeX
   * - Same as LaTex with 2 $'s
     - :math:`x=5`
   * - Same as LaTex with 2 $'s
     - :math:`\pi`
   * - Same as LaTex with 2 $'s
     - :math:`e = mc^{2}`


We can show all this directly *in* the Notebook!
$$\pi$$; $$e = mc^{2}$$; $$\int\ *{0}^{\inf} x^2 \,dx$$; $$\sum*\ {n=1}^{\infty} 2^{-n} = 1$$

Overleaf `has good documentation <https://www.overleaf.com/learn/latex/Main_Page>`_ for most (basic) applications.

Recap
"""""

..

   You will usually want to Google most things to do with laying out LaTeX code.


Resources
"""""""""


* `Jupyter Tips and Tricks <https://www.kaggle.com/tientd95/jupyter-notebook-tricks>`_
* `Pandoc Demos <https://pandoc.org/demos.html>`_
* `Beginner's Guide to Jupyter Notebooks <https://towardsdatascience.com/beginners-guide-to-jupyter-notebook-8bb85b85085>`_
* `7 Essential Tips to Writing With Jupyter Notebooks <https://towardsdatascience.com/7-essential-tips-for-writing-with-jupyter-notebook-60972a1a8901##699a>`_
* `Version Control with Jupyter <https://towardsdatascience.com/version-control-with-jupyter-notebook-b9630bc5996e>`_
* `Sustainable Publishing using Pandoc and Markdown <https://programminghistorian.org/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown>`_

Patterns in Text
~~~~~~~~~~~~~~~~

正则能匹配中文吗

正则的局限性

.. code-block:: python

   >>> '123foo456'.index('foo')
   2
   >>> '123foo456'.split('foo')
   ['123', '456']
   >>> ' 123 foo 456 '.strip() ### 移除首位空格
   '123 foo 456'
   >>> 'HOW NOW BROWN COW?'.lower()
   'how now brown cow?'
   >>> 'How now brown cow?'.replace('brown ','green-')
   'How now green-cow?'

Handling text
"""""""""""""

Regexes are a way for talking *about* patterns observed in text, although their origins are rooted in philosophy and linguistics.

Implemented in Python as:

.. code-block:: python

   import re
   ## re.search(<regex>, <str>)
   s = '123foo456'
   if re.search('123',s):
       print("Found a match.")
   else:
       print("No match.")

Prints ``'Found a match.'``

Capturing Matches
#################

.. code-block:: python

   m = re.search('123',s)
   print(m.start()) ## 0
   print(m.end())## 3
   print(m.span())## (0,3)
   print(m.group())## 123

^ So, we have ``None`` if a search fails, but if it succeeds then we have attributes of the ``match`` objection like start, end, span, and group (this last is going to be particularly interesting since it tells us what matched).

Configuring Matches
###################

.. code-block:: python

   m = re.search('FOO',s)
   print(m) ## None
   m = re.search('FOO',s,re.IGNORECASE)
   print(m) ## <re.Match object; span=(3, 6), match='foo'>

The third parameter allows us to: match newlines (\ ``re.DOTALL``\ ), ignore case (\ ``re.IGNORECASE``\ ), take language into account (\ ``re.LOCALE``\ ), match across lines (\ ``re.MULTILINE``\ ), and write patterns across multiple lines (\ ``re.VERBOSE``\ ). If you need multiple options it's ``re.DOTALL | re.IGNORECASE``. Bitwise again!

More Than One Match
###################

.. code-block:: python

   s = '123foo456foo789'
   lst = re.findall('foo',s)
   print(lst) ## ['foo','foo']
   lst = re.finditer('foo',s)
   [x for x in lst] ## ## [<re.Match object; span=(3, 6), match='foo'>, <re.Match object; span=(9, 12), match='foo'>]
   rs  = re.sub('foo',' ',s)
   print(rs)  ## '123 456 789'
   rs  = re.split(' ',rs)
   print(rs) ## ['123', '456', '789']

Regular Expression
""""""""""""""""""

.. code-block:: python

   >>> import re
   >>> m = re.search('\$((\d+,){2,}\d+)',
           "'That will be $1,000,000 he said...'")
   >>> m.group(1)
   '1,000,000'

This is not even scratching the surface, but it allows to look for sequences of 1-or-more digits followed by a comma... and for those sequence to repeat two or more times, ending with a sequence of digits. The rest is ignored.

Character Classes
#################

.. list-table::
   :header-rows: 1

   * - Characters
     - Regex Meta Class Options
     - 'Antonyms'
   * - a...z
     - ``[a-z]``\ , ``\w`` (word-like characters)
     - ``[^a-z]``\ , ``\W``
   * - A...Z
     - ``[A-Z]``\ , ``\w`` (word-like characters)
     - ``[^A-Z]``\ , ``\W``
   * - 0...9
     - ``[0-9]``\ , ``\d`` (digits)
     - ``[^0-9]``\ , ``\D``
   * - ``' '``\ , ``\n``\ , ``\t``\ , ``\r``\ , ``\f``\ , ``\v``
     - ``\s``
     - ``\S``
   * - ``.``\ , ``[``\ , ``]``\ , ``+``\ , ``$``\ , ``^``\ , ``|``\ , ``{``\ , ``}``\ , ``*``\ , ``(``\ , ``)``\ , ``?``
     - For safety always precede character with a ``\``.
     - None


*Note:*  ``\w`` will include ``_``. And ``\`` is, once again, important as it 'escapes' various characters, and options.

Options
#######

.. list-table::
   :header-rows: 1

   * - Options
     - Regex Meta Class Options
   * - **i**
     - 不区分大小写匹配, 它把字母 A 到 Z 视为等同于它们的小写副本.
   * - **m**
     - 多行. 把\ *Haystack*\ 视为许多单独的行（如果它包含新行符）的集合而不是一个单个的连续行。具体地, 它会改变下列方式:1) 抑扬符 (^) 能匹配紧跟在内部所有新行符之后的位置, 如同它总能匹配 *Haystack* 的开始处一样 (但它不会匹配 *Haystack* 的 *最后面* 的新行符之后的位置).2) 美元符 ($) 能匹配 *Haystack* 中任何新行符之前的位置 (如同它总能匹配最后面的位置).例如，模式“m)^abc$”中包含了“m”选项才能在 *Haystack*\ “xyz\ ``r``\ nabc”中形成匹配。使用了 "m" 选项时 "D" 选项会被忽略.
   * - **s**
     - DotAll. 此选项会让句点 (.) 匹配包含新行符在内的所有字符 (一般情况下, 它不能匹配新行符). 然而, 如果换行符是默认的 CRLF (\ ``r``\ n), 则必须使用两个句点才能进行匹配 (不是一个). 不论是否使用此选项, 排除型字符类 (例如 [^a]) 总能匹配新行符.
   * - **x**
     - 忽略模式中的空白字符, 除非对它们进行转义或出现在字符类中. 字符 ``n 和``\ t 在它们达到 PCRE 时会被忽略, 因为它们已经是原始的/原义的空白字符 (与之相比, \n 和 \t 则不会被忽略, 因为它们是 PCRE 的转义序列). **x** 选项还会忽略字符类外面的非转义 ## 和下一个新行符之间的字符 (包括它们). 这使得在复杂的模式中添加注释成为可能. 然而, 这只适用于数据字符; 空白字符可能永远都不会出现在特殊字符序列中, 例如 (?(, 它以条件子模式开头.
   * - **A**
     - 强制固定匹配模式; 即它只能匹配 *Haystack* 的开始处 (即使开始处是换行符, 也会从换行符开始匹配而不从换行符之后的字符开始). 在大多数条件下, 它的作用等同于在模式中使用 "^".
   * - **D**
     - 强制美元符 ($) 匹配 *Haystack* 的末端, 即使 *Haystack* 的最后的字符是新行符. 如果没有此选项，则$会匹配最后的新行符之前的位置（如果有新行符，此时匹配不会包括新行符）。注: 使用了 "m" 选项时此选项会被忽略.
   * - **J**
     - 允许重复 `命名子模式 <https://ahkcn.github.io/docs/commands/RegExMatch.htm##NamedSubPat>`_. 它可用于在一组相同的命名子模式中只有其中一个形成匹配的模式. 注: 如果有多个特殊名子模式的实例形成匹配, 那么只保存最左边的那个. 此外, 变量名不区分大小写.
   * - **U**
     - 非贪婪. 让限定符 *+?{} 在形成匹配时只消耗必需的那些字符, 把剩下的部分留给模式的后面部分. 没有使用 "U" 选项时, 可以在这些字符后加上问号来限定它们为非贪婪的. 相反地, *\ 使用了* "U" 选项时, 问号会成为贪婪匹配的限定符.
   * - **X**
     - PCRE_EXTRA. 启用不兼容 Perl 的 PCRE 功能. 目前, 这样的唯一功能是在模式中的任意反斜线后跟着没有特殊含义的字母时会导致匹配失败并因此设置 ErrorLevel. 此选项会帮助保留未使用的反斜线序列供将来使用. 如果没有此选项, 反斜线后跟着没有特殊含义的字母时会被视为原义的 (即 \g 和 g 都被识别为原义的 g). 不论是否使用此选项, 没有特殊含义的非字母反斜线序列总是被视为原义的 (即 \/ 和 / 都被视为正斜杠).
   * - **P**
     - 位置模式. 这会使 RegExMatch() 产生匹配和其子模式的位置和长度而不是匹配它们的子字符串. 更多细节请参阅 `UnquotedOutputVar <https://ahkcn.github.io/docs/commands/RegExMatch.htm##PosMode>`_\ 。
   * - **S**
     - 研究模式来提高性能. 它可用于要执行多次的特殊模式 (尤其是复杂的模式). 如果 PCRE 找到了提高性能的方法, 则会把这个发现储存到缓存中模式的旁边, 以便在之后执行相同模式时使用 (后续使用此模式时还需要指定 S 选项, 因为要找到缓存中相同的模式则它们的选项也必须完全相同, 包括它们的顺序). (这里的研究主要指在进行匹配前使用其他一些通常较简单快速的方法进行判断, 例如假设模式至少匹配 5 个字符, 而源字符串只有 3 个, 那么正则表达式引擎会直接返回 "没有匹配" 的结果, 而不会进行匹配.)
   * - **C**
     - 启用自动调出模式。请参阅\ `正则表达式调出 <https://ahkcn.github.io/docs/misc/RegExCallout.htm##auto>`_\ 了解更多信息。
   * - **`n**
     - 从默认的新行符 (\ ``r``\ n) 切换到单独的换行符 (`n), 这是 UNIX 系统的标准. 所选择的新行符会影响 `锚 (^ 和 $) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##anchor>`_ 和 `含句点的模式 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##dot>`_.
   * - **`r**
     - 从默认的新行符 (\ ``r``\ n) 切换到单独的回车符 (`r).
   * - **`a**
     - 在 v1.0.46.06+, ``a 可以识别任意类型的新行符, 即``\ r, ``n,``\ r\ ``n,``\ v/VT/vertical tab/chr(0xB), ``f/FF/formfeed/chr(0xC) 以及 NEL/next-line/chr(0x85). 在 v1.0.47.05+，新行符可以被限制为 CR、LF 和 CRLF 三种，只需要在模式的开始处（选项后面）指定大写的（*ANYCRLF）；例如``\ im)(*ANYCRLF)^abc$`。


Metacharacters
##############

.. list-table::
   :header-rows: 1

   * - Metacharacter
     - Meaning
   * - .
     - Any character at all
   * - ^
     - Start of a string/line
   * - $
     - End of a string/line
   * - *
     - 0 or more of something
   * - +
     - 1 or more of something
   * - ?
     - 0 or 1 of something; also lazy modifier
   * - {m,n}
     - Between m and n of something
   * - [ ]
     - A set of character literals
   * - ( )
     - Group/remember this sequence of characters
   * - |
     - Or


.. list-table::
   :header-rows: 1

   * - Metacharacter
     - Meaning
   * - **.**
     - 默认情况下, 句点匹配除新行符 (\ ``r``\ n) 序列外的任何单个字符, 但是这种特性可以使用 `DotAll (s) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##opt_s>`_\ , `新行 (`n) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##opt_esc_n>`_\ , `回车 (`r) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##opt_esc_r>`_\ , ``a 或 (*ANYCRLF) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##NEWLINE_ANY>`_ 选项进行改变. 例如, **ab.** 可以匹配 abc 和 abz 以及 ab_.
   * - *****
     - 星号匹配零个或多个前面的字符, `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##class>`_ 或 `子模式 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##subpat>`_. 例如, **a*** 可以匹配 ab 和 aaab. 它还可以匹配完全不包含 "a" 的任意字符串的开始处.\ **通配符:** 句点星号模式 **.*** 是匹配范围最广的模式之一, 因为它可以匹配零个或多个 *任意* 字符 (除了新行符: ``r 和``\ n). 例如, **abc.*123** 可以匹配 abcAnything123, 也能匹配 abc123.
   * - **?**
     - 问号匹配零或一个前面的字符, `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##set>`_ 或 `子模式 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##subpat>`_. 可以理解为 "前面的那项是可选的". 例如, **colou?r** 可以匹配 color 和 colour, 因为 "u" 是可选的.
   * - **+**
     - 加号匹配一个或多个前面的字符, `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##class>`_ 或 `子模式 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##subpat>`_. 例如 **a+** 可以匹配 ab 和 aaab. 但与 **a*** 和 **a?** 不同的是, 模式 **a+** 不会匹配开始处没有 "a" 的字符串.
   * - {min,max}
     - 匹配出现次数介于 *min* 和 *max* 的前面的字符, `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##set>`_ 或 `子模式 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##subpat>`_. 例如, **a{1,2}** 可以匹配 ab 但只匹配 aaab 中的前两个 a.此外, {3} 表示准确匹配 3 次, 而 {3\ **,**\ } 则表示匹配 3 次或更多. 注: 指定的数字必须小于 65536, 且第一个必须小于等于第二个.
   * - **[...]**
     - **字符类:** 方括号把一列字符或一个范围括在了一起 (或两者). 例如, **[abc]** 表示 "a, b 或 c 的中任何一个字符". 使用破折号来创建范围; 例如, **[a-z]** 表示 "在小写字母 a 和 z (包含的) 之间的任何一个字符". 列表和范围可以组合在一起; 例如 **[a-zA-Z0-9_]** 表示 "字母, 数字或下划线中的任何一个字符".字符类后面可以使用 *, ?, + 或 {min,max} 进行限定. 例如, **[0-9]+** 匹配一个或多个任意数字; 因此它可以匹配 xyz123 但不会匹配 abcxyz.通过 [[:xxx:]] 还支持下列 POSIX 命名集, 其中 xxx 是下列单词的其中一个: alnum, alpha, ascii (0-127), blank (space 或 tab), cntrl (控制字符), digit (0-9), xdigit (十六进制数), print, graph (排除了空格的打印字符), punct, lower, upper, space (空白), word (等同于 `\w <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##word>`_\ ).在字符类中, 只有在类中具有特殊含义的字符才需要进行转义; 例如 **[\^a]**\ , **[a-b]**\ , **[a]]** 和 **[\a]**.
   * - **[^...]**
     - 匹配 **不** 在类中的任何一个字符. 例如, **[^/]*** 匹配零个或多个 *不是* 正斜杠的任意字符, 例如 http://. 同样地, **[^0-9xyz]** 匹配既不是数字也不是 x, y 或 z 的任何一个字符.
   * - **\d**
     - 匹配任意一个数字 (相当于类 **[0-9]**\ ). 相反地，大写的\D表示“任意的\ *非*\ 数字字符”。这个和下面的两个都可以用在 `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##set>`_ 中; 例如, **[\d.-]** 表示 "任何数字, 句点或负号".
   * - **\s**
     - 匹配任意单个空白字符 , 主要是空格, tab 和新行符 (\ ``r 和``\ n). 相反地, 大写的 \S 表示 "任何 *非*\ 空白字符".
   * - **\w**
     - 匹配任何单个 "单词" 字符, 即字母, 数字或下划线. 这等同于 **[a-zA-Z0-9_]**. 相反地, 大写的 \W 表示 "任何 *非*\ 单词字符".
   * - **^ $**
     - 抑扬符 (^) 和美元符 ($) 被称为 *锚*\ , 因为它们不消耗任何字符; 相反地, 它们把模式限定在被搜索字符串的开始或末尾进行匹配.在模式的开始处使用 **^** 表示需要在行的开始处进行匹配. 例如, **^abc** 可以匹配 abc123 但不匹配 123abc.在模式的末尾处使用 **$** 表示需要在行的末端进行匹配. 例如, **abc$** 可以匹配 123abc 但不能匹配 abc123.这两个锚还可以组合使用. 例如, **^abc$** 仅匹配 abc (即在它的前面或后面不能有另外的字符).如果被搜索的文本包含多行, 则可以使用 `"m" 选项 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##Multiline>`_ 让锚应用于每行而不是把所有文本作为整体. 例如, **m)^abc$** 可以匹配 123\ ``r``\ nabc\ ``r``\ n789. 但如果没有 "m" 选项, 则不会形成匹配.
   * - **\b**
     - \b 表示 "单词边界", 它类似锚, 因为它不消耗任何字符. 它要求当前字符的 `状态为单词字符 (\w) <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##word>`_\ , 与前一个字符的状态相反. 它通常用来避免意外地匹配到在其他单词内的某个单词. 例如, **\bcat\b** 不会匹配 catfish, 但它可以匹配不论周围是否有标点或空白的 cat. 大写的 \B 则相反: 它要求当前字符 *不是* 单词的边界.
   * - **|**
     - 竖线将两个或多个可选项目分隔开来. 如果可选项目中 *任何一个* 满足条件, 则会形成匹配. 例如, **gray|grey** 既可以匹配 gray 也可以匹配 grey. 同样地, 模式 **gr(a|e)y** 中通过下面描述的括号的帮助可以实现同样的作用.
   * - **(...)**
     - 括在括号中的项目常用于:确定求值的顺序. 例如, **(Sun|Mon|Tues|Wednes|Thurs|Fri|Satur)day** 可以匹配任何一天的名称.把 *****\ , **?**\ , **+** 或 **{min,max}** 应用到 *系列* 字符而不只是单个字符. 例如, **(abc)+** 匹配一个或一串字符串 "abc"; 因此它可以匹配 abcabc123 但不会匹配 ab123 或 bc123.捕获子模式, 例如 **abc(.*)xyz** 中的句点星号. 例如, `RegExMatch() <https://ahkcn.github.io/docs/commands/RegExMatch.htm>`_ 会把匹配每个子模式的子字符串保存到 `输出数组 <https://ahkcn.github.io/docs/commands/RegExMatch.htm##Array>`_. 同样地, `RegExReplace() <https://ahkcn.github.io/docs/commands/RegExReplace.htm>`_ 中允许把匹配每个子模式的子字符串通过像 $1 这样的 `后向引用 <https://ahkcn.github.io/docs/commands/RegExReplace.htm##BackRef>`_ 重新插入到替换结果中. 要使用不捕获子模式的括号, 请把括号内的开始两个字符指定为 **?:**\ ; 例如: **(?:.*)**\ 在匹配过程中改变 `选项 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##Options>`_. 例如, **(?im)** 会为模式的后续部分打开不区分大小写和多行选项 (如果它在子模式中则它会改变子模式的选项). 相反地, **(?-im)** 会关闭它们. 支持除 DPS\ ``r``\ n`a 外的所有选项.
   * - **\t \r 等等.**
     - 这些转义序列表示特殊的字符. 最常见的有 **\t** (tab), **\r** (回车) 和 **\n** (换行). 在 AutoHotkey, 在这些情况中还可以使用重音符 (\ ``) 代替反斜线. 还支持 \xhh 格式的转义序列, 其中 *hh* 是介于 00 和 FF 之间的任意 ANSI 字符的十六进制码.在 v1.0.46.06+, **\R** 表示 "单个任意类型的新行符", 即在 [``\ a 选项](https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##NEWLINE_ANY) 中列出的这些 (然而, \R 在 `字符类 <https://ahkcn.github.io/docs/misc/RegEx-QuickRef.htm##class>`_ 中仅仅表示字母 "R"). 在 v1.0.47.05+, **\R** 可以被限制为 CR, LF 和 CRLF 三种, 只需要在模式的开始处 (选项后面) 指定大写的 (\ *BSR_ANYCRLF) ; 例如 **im)(\*\ BSR_ANYCRLF)abc\Rxyz**
   * - **\p{xx} \P{xx} \X**
     - [AHK_L 61+]: Unicode 字符属性. 在 ANSI 版本中不支持. **\p{xx}** 匹配带 xx 属性的字符而 **\P{xx}** 匹配 *不带* xx 属性的任意一个字符. 例如, **\pL** 匹配任意一个字母而 **\p{Lu}** 匹配任意一个大写字母. **\X** 匹配组成扩展 Unicode 序列的任何数目的字符.对于受支持的属性名称的完整列表和其他细节, 请在 `www.pcre.org/pcre.txt <http://www.pcre.org/pcre.txt>`_ 中搜索 "\p{xx}".
   * - **(*UCP)**
     - [AHK\ *L 61+]: 考虑到性能, \d, \D, \s, \S, \w, \W, \b 和 \B 默认情况下只识别 ASCII 字符, 即使在 Unicode 版本中也是如此. 如果模式以 **(*UCP)** 开头, 则会使用 Unicode 属性来判断哪个字符匹配. 例如, \w 变成相当于 **[\p{L}\p{N}*\ ]\ ** 而 \d 变成等同于 **\ \p{Nd}**.


**贪婪**\ ：默认情况下，\ *****\ 、\ **?**\ 、\ **+** 和 **{min,max}** 是贪婪的，因为它们消耗到\ *最后一个*\ 能满足整个模式的可能的所有字符。要让它们停在 *首个* 可能的字符, 请在它们后面加上问号. 例如, 模式 **<.+>** (其中没有问号) 表示: "搜索一个 <, 接着一个或多个任意字符, 然后是一个 >". 要在匹配 *整个* 字符串 **<**\ em>text</em\ **>** 时停止, 请在加号后加上问号: **<.+?>**. 这样会让匹配在第一个 '>' 处停止, 因此它只匹配第一个标签 **<**\ em\ **>**.

**预测和回顾断言**\ ：这组 **(?=...)**\ 、\ **(?!...)**\ 、\ **(?<=...)** 和 **(?<!...)** 被称为\ *断言*\ ，因为它们要求符合某个条件但不消耗任何字符。例如, **abc(?=.*xyz)** 中含有预测断言, 它要求在字符串 abc 右边的某个位置存在字符串 xyz (如果不存在, 则匹配失败). **(?=...)** 被称为 *正* 预测断言, 因为它要求指定的模式存在. 相反地, **(?!...)** 是 *负* 预测断言, 因为它要求指定的模式 *不* 存在. 同样地, **(?<=...)** 和 **(?<!...)** 分别是正的和负的 *回顾* 断言, 因为它们检查当前位置的 *左边* 而不是右边. 回顾比预测受到更多的限制, 因为它们不支持可变大小的限定符, 例如 *****\ , **?** 和 **+**. 转义序列 \K 类似于回顾断言, 因为它会让前一个匹配的字符在最后的匹配字符串中省略. 例如, **foo\Kbar** 可以匹配 "foobar" 但报告匹配的结果为 "bar".

Building Blocks
###############

.. list-table::
   :header-rows: 1

   * - Regex
     - Interpretation
   * - ``r'\s*'``
     - 0 or more spaces
   * - ``r'\d+'``
     - 1 or more digits
   * - ``r'[A-Fa-f0-7]{5}'``
     - Exactly 5 hexadecimal 'digits'
   * - ``r'\w+\.\d{2,}'``
     - 1 or more 'wordish' characters, followed by a full-stop, then 2 or more digits
   * - ``r'^[^@]+@\w+'``
     - One more non-@ characters at the start of a line, followed by a '@' then 1 or more 'wordish' characters.
   * - ``r'(uk|eu|fr)$'``
     - The characters 'uk' or 'eu' or 'fr' at the end of a line.


Examples
########

.. code-block:: python

   re.match(r'^[^@]+@([a-z0-9\-]+\.){1,5}[a-z0-9\-]+$', s)

   re.match(r'\d{4}-\d{2}-\d{2}', s)

   re.match(r'^\s*$', s)

   re.match(r'^(http|https|ftp):[\/]{2}([a-zA-Z0-9\-]+\.){1,4}[a-zA-Z]{2,5}(:[0-9]+)?\/?([a-zA-Z0-9\-\._\?\'\/\\\+\&\%\$##\=~]*)',s)

   re.match(r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})',s)

   regex = r"""
   ([GIR] 0[A]{2})|    ## Girobank 
   (
     (
       ([A-Z][0-9]{1,2})| ## e.g A00...Z99
         (
           ([A-Z][A-HJ-Y][0-9]{1,2})|  ## e.g. AB54...ZX11
             (([A-Z][0-9][A-Z])|  ## e.g. A0B...Z9Z 
             ([A-Z][A-HJ-Y][0-9][A-Z]?))  ## e.g. WC1 or WC1H
           )
         )
       \s?[0-9][A-Z]{2} ## e.g. 5RX
     )
   """
   re.match(regex,s,re.VERBOSE|re.IGNORECASE) ## Can also use: re.X|re.I

^ This is the `government's own regex <https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/488478/Bulk_Data_Transfer_-_additional_validation_valid_from_12_November_2015.pdf>`_ but is probably *not* 100% accurate.

Resources
#########


* `Python Documentation <https://docs.python.org/3/howto/regex.html>`_
* `Real Python: Regular Expressions 1 <https://realpython.com/regex-python/>`_
* `Real Python: Regular Expressions 2 <https://realpython.com/regex-python-part-2/>`_
* `Data Camp RegEx Tutorial <https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial>`_
* `Introduction to Regex <https://medium.com/better-programming/introduction-to-regex-8c18abdd4f70>`_
* `Understanding RegExes in Python <https://medium.com/better-programming/introduction-to-regex-8c18abdd4f70>`_
* `Demystifying RegExes in Python <https://medium.com/@snk.nitin/your-guide-to-using-regular-expressions-in-python-a7908b8e4b68>`_
* `Python RegExes <https://medium.com/@devopslearning/python-regular-expression-8ee28d35f3a7>`_
* `Mastering String Methods in Python <https://towardsdatascience.com/mastering-string-methods-in-python-456174ede911>`_

Thanks to `Yogesh Chavan <https://levelup.gitconnected.com/extremely-useful-regular-expression-examples-for-real-world-applications-567e844a0822>`_ and `Nicola Pietroluongo <https://www.sitepoint.com/demystifying-regex-with-practical-examples/>`_ for examples.

Cleaning Text
~~~~~~~~~~~~~

Vectorisation & Parallelisation
"""""""""""""""""""""""""""""""

Pandas.apply() vs. Numpy
########################

Numpy is fully vectorised and will almost *always* out-perform operations like Pandas ``apply``\ , but both are massive improvements on for loops:


* Execute row-wise and column-wise operations.
* Apply any arbitrary function to individual elements or whole axes.
* Can make use of ``lambda`` functions too for 'one off' operations.

.. code-block:: python

   import numpy as np
   df.apply(np.sqrt) ## Square root of all values
   df.apply(np.sum, axis=0) ## Sum by row

Lambda Functions
################

.. code-block:: python

   >>> x = lambda a : a + 10
   >>> print(x(5))
   15

Or:

.. code-block:: python

   >>> full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
   >>> full_name('guido', 'van rossum')
   'Guido Van Rossum'

Dealing with Structured Text
""""""""""""""""""""""""""""

Beautiful Soup & Selenium
#########################

Two stages to acquiring web-based documents:


#. Accessing the document: ``urllib`` can deal with many issues (even authentication), but *not* with dynamic web pages (which are increasingly common); for that, you need `Selenium <https://selenium-python.readthedocs.io/>`_ (library + driver).
#. Processing the document: simple data can be extracted from web pages with RegularExpressions, but *not* with complex (esp. dynamic) content; for that, you need `BeautifulSoup4 <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_.

These interact with wider issues of Fair Use (e.g. rate limits and licenses); processing pipelines (e.g. saving WARCs or just the text file, multiple stages, etc.); and other practical constraints.

Regular Expressions / Breaks
############################

Need to look at how the data is organised:


* For very large corpora, you might want one document at a time (batch).
* For very large files, you might want one line at a time (streaming).
* For large files in large corpora, you might want more than one machine.

^ See the `OpenVirus Project <https://blogs.bl.uk/digital-scholarship/2020/05/searching-etheses-for-the-openvirus-project.html>`_.

Managing Vocabularies
"""""""""""""""""""""

Starting Points
###############

These strategies can be sued singly or all-together:


* Stopwords
* Case
* Accent-stripping
* Punctuation
* Numbers

Sample stopwords:

.. code-block:: python

   {'further', 'her', 'their', 'we', 'just', 'why', 'or', 'each', 's', "it's", 'ma', 'below', 'am', 'more', "couldn't", "should've", 'was', "mightn't", 'weren', 'ourselves', 'have', 'if', 'then', 'from', ...}

But these are just a *starting* point!

^ What's the semantic difference between 1,000,000 and 999,999?

Distributional Pruning
######################

We can prune from both ends of the distribution:


* Overly rare words: what does a word used in *one* document help us to do?
* Overly common ones: what does a word used in *every* document help us to do?

^ Again, no hard-and-fast rules: can be done on raw counts, percentage of all documents, etc. Choices will, realistically, depend on the nature of the data.

Stemming & Lemmatisation
""""""""""""""""""""""""

Why Stem or Lemmatise?
######################

Reduce the breadth of human expression:


* Porter & Snowball Stemming: rules-based truncation to a stem (can be augmented by language awareness).
* Lemmatisation: dictionary-based 'deduplication' to a lemma (can be augmented by POS-tagging).

Compare:

.. list-table::
   :header-rows: 1

   * - Source
     - Porter
     - Snowball
     - Lemmatisation
   * - monkeys
     - monkey
     - monkey
     - monkey
   * - cities
     - citi
     - citi
     - city
   * - complexity
     - complex
     - complex
     - complexity
   * - Reades
     - read
     - read
     - Reades


Resources
"""""""""


* `Vectorisation in Python <https://towardsdatascience.com/python-vectorization-5b882eeef658>`_
* `Lambda Functions <https://www.w3schools.com/python/python_lambda.asp>`_
* `Real Python Lambda Functions <https://realpython.com/python-lambda/>`_
* `Stemming words with NLTK <https://pythonprogramming.net/stemming-nltk-tutorial/>`_
* `Stemming and Lemmatisation in Python <https://www.datacamp.com/community/tutorials/stemming-lemmatization-python>`_
* `KD Nuggets: A Practitioner's Guide to NLP <https://www.kdnuggets.com/2018/08/practitioners-guide-processing-understanding-text-2.html>`_
* `KD Nuggets: Linguistic Fundamentals for Natural Language Processing: 100 Essentials from Semantics and Pragmatics <https://www.kdnuggets.com/2020/08/linguistic-fundamentals-natural-language-processing.html>`_
* `Roadmap to Natural Language Processing (NLP) <https://www.kdnuggets.com/2020/10/roadmap-natural-language-processing-nlp.html>`_

Analysing Text
~~~~~~~~~~~~~~

One-Hot Encoding
""""""""""""""""

May already be familiar with concept as 'dummy variables' in economics/regression:

.. list-table::
   :header-rows: 1

   * - Document
     - UK
     - Top
     - Pop
     - Coronavirus
   * - News
     - 1
     - 1
     - 0
     - 1
   * - Culture
     - 0
     - 1
     - 1
     - 0
   * - Politics
     - 1
     - 0
     - 0
     - 1
   * - Entertainment
     - 1
     - 1
     - 1
     - 1


^ Certainly One-Hot encoders are rarely, if ever, used this way, but for keyword detection this might be appropriate: i.e. this word was used in this document!

^ Only difference is One Hot == $$n$$ variables, Dummy == $$n-1$$.

^ Definitely some 'gotchas' in deployment: one-hot models shouldn't have an intercept unless you apply a 'ridge shrinkage penalty'. Standardisation affects whether or not an intercept is needed.

The 'Bag of Words'
""""""""""""""""""

Could simply be seen as an extension of binarised approach on preceding slide:

.. list-table::
   :header-rows: 1

   * - Document
     - UK
     - Top
     - Pop
     - Coronavirus
   * - News
     - 4
     - 2
     - 0
     - 6
   * - Culture
     - 0
     - 4
     - 7
     - 0
   * - Politics
     - 3
     - 0
     - 0
     - 3
   * - Entertainment
     - 3
     - 4
     - 8
     - 1


BoW in Practice
"""""""""""""""

Enter, stage left, `scikit-learn <https://scikit-learn.org/stable/>`_\ :

.. code-block:: python

   from sklearn.feature_extraction.text import CountVectorizer
   vectorizer = CountVectorizer()

   vectorizer.fit(texts)
   vectors = vectorizer.transform(texts)

   ## Same thing:
   ## vectors = vectorizer.fit_transform(texts)

   print(f'Vocabulary: {vectorizer.vocabulary_}')
   print(f'Full vector: {vectors.toarray()}')

TF/IDF
""""""

Builds on Count Vectorisation by normalising the document frequency measure by the overall corpus frequency. Common words receive a large penalty:

$$
W(t,d) = TF(t,d) / log(N/DF_{t})
$$

For example: if the term 'cat' appears 3 times in a document of 100 words then $TF(t,d)=3/100$. If there are 10,000 documents and cat appears in 1,000 documents then $N/DF_{t}=10000/1000$ and $log(10)=1$, so IDF=1 and TF/IDF=0.03.

TF/IDF in Practice
##################

.. code-block:: python

   from sklearn.feature_extraction.text import TfidfVectorizer
   vectorizer = TfidfVectorizer()

   vectorizer.fit(texts)
   vectors = vectorizer.transform(texts)

   ## Same thing:
   ## vectors=vectorizer.fit_transform(texts)

   print(f'Vocabulary: {vectorizer.vocabulary_}')
   print(f'Full vector: {vectors.toarray()}')

^ What do you notice about how this code differs from the CountVectorizer?

Term Co-Occurence Matrix (TCM)
""""""""""""""""""""""""""""""

Three input texts:


* the cat sat on the mat
* the cat sat on the fluffy mat
* the fluffy ginger cat sat on the mat

.. list-table::
   :header-rows: 1

   * - 
     - fluffy
     - mat
     - ginger
     - sat
     - on
     - cat
     - the
   * - fluffy
     - 
     - 1
     - 1
     - 
     - 0.5
     - 0.5
     - 2.0
   * - mat
     - 
     - 
     - 
     - 
     - 0.5
     - 
     - 1.5
   * - ginger
     - 
     - 
     - 
     - 0.5
     - 0.5
     - 1.0
     - 1.5
   * - sat
     - 
     - 
     - 
     - 
     - 3.0
     - 3.0
     - 2.5
   * - on
     - 
     - 
     - 
     - 
     - 
     - 1.5
     - 3.0
   * - cat
     - 
     - 
     - 
     - 
     - 
     - 
     - 2.0
   * - the
     - 
     - 
     - 
     - 
     - 
     - 


Text2Vec & word embedding
"""""""""""""""""""""""""

Typically some kind of 2 or 3-layer neural network that 'learns' (using as big a training data set as possible) how to embed the TCM into a lower-dimension representation. 

Conceptual similarities to PCA in terms of what we're trying to achieve, but the *process* is utterly different.

Many different approaches, but `GloVe <https://nlp.stanford.edu/projects/glove/>`_ (Stanford), `word2vec <https://code.google.com/archive/p/word2vec/>`_ (Google), `fastText <https://fasttext.cc/docs/en/english-vectors.html>`_ (Facebook), and `ELMo <https://allennlp.org/elmo>`_ (Allen) or `BERT <https://github.com/google-research/bert>`_ (Google) are probably the best-known.

Sentiment Analysis
""""""""""""""""""

Requires us to deal in great detail with bi- and tri-grams because *negation* and *sarcasm* are hard. Also tends to require training/labelled data.


.. image:: http://www.zzzhou.me/images/2020/11/25/Sentiment_Analysis.png
   :target: http://www.zzzhou.me/images/2020/11/25/Sentiment_Analysis.png
   :alt: Sentiment_Analysis


`A Sentiment Analysis Approach to Predicting Stock Returns <https://medium.com/@tomyuz/a-sentiment-analysis-approach-to-predicting-stock-returns-d5ca8b75a42>`_

Clustering
""""""""""

.. list-table::
   :header-rows: 1

   * - Cluster
     - Geography
     - Earth Science
     - History
     - Computer Science
     - Total
   * - 1
     - 126
     - 310
     - 104
     - 11,018
     - 11,558
   * - 2
     - 252
     - 10,673
     - 528
     - 126
     - 11,579
   * - 3
     - 803
     - 485
     - 6,730
     - 135
     - 8,153
   * - 4
     - 100
     - 109
     - 6,389
     - 28
     - 6,626
   * - Total
     - 1,281
     - 11,577
     - 13,751
     - 11,307
     - 37,916


Topic Modelling
"""""""""""""""

Learning associations of words (or images or many other things) to hidden 'topics' that generate them:

LDA

Resources
"""""""""


* `One-Hot vs Dummy Encoding <https://stats.stackexchange.com/questions/224051/one-hot-vs-dummy-encoding-in-scikit-learn>`_
* `Categorical encoding using Label-Encoding and One-Hot-Encoder <https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd>`_
* `Count Vectorization with scikit-learn <https://towardsdatascience.com/natural-language-processing-count-vectorization-with-scikit-learn-e7804269bb5e>`_
* `TFIDF.com <http://www.tfidf.com/>`_
* `The TF*IDF Algorithm Explained <https://www.onely.com/blog/what-is-tf-idf/>`_
* `How to Use TfidfTransformer and TfidfVectorizer <https://kavita-ganesan.com/tfidftransformer-tfidfvectorizer-usage-differences/##.X7gXhhP7Tlw>`_
* `SciKit Learn Feature Extraction <https://scikit-learn.org/stable/modules/classes.html##module-sklearn.feature_extraction>`_
* `Your Guide to LDA <https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d>`_
* `Machine Learning — Latent Dirichlet Allocation LDA <https://jonathan-hui.medium.com/machine-learning-latent-dirichlet-allocation-lda-1d9d148f13a4>`_
* `A Beginner’s Guide to Latent Dirichlet Allocation(LDA) <https://towardsdatascience.com/latent-dirichlet-allocation-lda-9d1cd064ffa2>`_
* `Analyzing Documents with TF-IDF <https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf>`_

Basically any of the lessons on `The Programming Historian <https://programminghistorian.org/en/lessons/>`_.

----

More Resources
~~~~~~~~~~~~~~


* `Introduction to Word Embeddings <https://towardsdatascience.com/introduction-to-word-embeddings-4cf857b12edc>`_
* `The Current Best of Universal Word Embeddings and Sentence Embeddings <https://medium.com/huggingface/universal-word-sentence-embeddings-ce48ddc8fc3a>`_
* `Using GloVe Embeddings <http://text2vec.org/glove.html>`_
* `Working with Facebook's FastText Library <https://stackabuse.com/python-for-nlp-working-with-facebook-fasttext-library/>`_
* `Word2Vec and FastText Word Embedding with Gensim <https://towardsdatascience.com/word-embedding-with-word2vec-and-fasttext-a209c1d3e12c>`_
* `Sentence Embeddings. Fast, please! <https://towardsdatascience.com/fse-2b1ffa791cf9>`_
* `PlasticityAI Embedding Models <https://github.com/plasticityai/magnitude>`_
* `Clustering text documents using *k*\ -means <https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html##sphx-glr-auto-examples-text-plot-document-clustering-py>`_
* `Topic extraction with Non-negative Matrix Factorization and LDA <https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html##sphx-glr-auto-examples-applications-plot-topics-extraction-with-nmf-lda-py>`_

Agenda
^^^^^^

Agenda
~~~~~~


* Different plotting options: https://stackoverflow.com/a/37970713

  * Short Answer: you don't, I'm a creature of habit and lazy.
  * Longer Answer: I prefer to show you *one* way that works generally, than two or three different ways that require you to change your code for each.

* Floating Point Arithmetic

  * Hat tip for this: https://github.com/jreades/i2p/issues/15
  * Floating Point errors are a *fundamental* cause of problems in many applications and they are *hard* to debug.

Techniques
~~~~~~~~~~


* CSLs and LaTeX:

  * Short answer: `no <https://tex.stackexchange.com/a/69284>`_
  * For full LaTeX bibliographies you will need either BibLaTeX or Biber as these are more powerful and offer more options.
  * CSLs are for pandoc alone AFAIK.
  * Here's a nice RMarkdown tutorial: https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html

* RegExes

  * Part 1: ``[A-F]`` has the special meaning 'A-through-F' (i.e. ``A|B|C|D|E|F``\ ); whereas the ``{m,n}`` syntax is for something *repeating* between ``m`` and ``n`` times (inclusive). So ``m`` and ``n`` must be numeric. I think you're being misled by Python's dictionary sytnax?
  * Part 2: ``^`` has *two* meanings:

    * Inside a ``[...]`` and as the first character it means *not* (i.e. ``[^A-F]``\ ) would negate 'A-through-F'.
    * At the start of a regular expression it means *at the start of a line* (i.e. ``r'^A'`` would match lines starting with an ``A``\ ).

* Fit/Transform

  * Fitting and transformation do not have to happen at the same time.
  * But fitting cannot be updated *afterwards* as the mapping/weights have been calculated.
  * So values that weren't fitted are likely to be dropped during the transform stage because there's no mapping/weight for them.
  * You might have separate fit and transform calls if you don't want to/need to transform all of your data at once and only want to transform parts of the full data set. So you fit once and then transform multiple times.
  * You might also have separate fit and transform calls if your data is streaming (but see limitation above).

* How you do you add a bib file to Markdown?

  * Yes, only pandoc can make sense of the bib file *in Markdown*. 
  * LaTeX can process bib files too though.

Concepts
~~~~~~~~


* Can we measure the complexity of a text?

  * Up to a point: there are all sorts of ways to measure this! What is meaningful depends on the language, sentence structure, grammar, etc.! 

* Shared readings!!!

  * https://collections.plos.org/collection/science-of-stories/
  * https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0225385
  * There are a lot more on this! Great finds though!

Triumphs
~~~~~~~~


* 
  Using ``numpy``


  * Very nice! 🎩tip
  * Using numpy directly will definitely represent a speed-up, but you would only benefit for queries that numpy can cope with (primarily NaNs and Numbers--which is a pretty big span!)

* 
  Pronunciation


  * Hah, hah, you're not the only one!

Workshop
^^^^^^^^
