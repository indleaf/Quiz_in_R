question_bank = [
    # Q1–Q5
    {"question": "In graph theory, the term incident is when two vertices are connected via an edge.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "Graph databases use SQL to implement a query.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "Processing Complex queries, graph databases are faster that relational databases.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "In ggplot2 the component responsible for mapping data frame variables and determining visual properties is the aesthetics.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "A data frame in R is used to group together any mix of data structures and objects.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},

    # Q6–Q10
    {"question": "The outcome of the if statement below is True\nIf(15%%4 <= 3 & 2^4 >15)",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "The igraph statement below will create a directed graph made of two vertices, one edge and one loop.\nG <- graph(c(1,2, 2,2 1,1), n=2)",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "In graph theory, the term loop is an edge that has the same start and end vertex.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "The result of the statement below is 0.\ncat(mean(seq(1,3))%%2)",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "The if statement below returns True\nif((16%%3)^9999)",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},

    # Q11–Q15
    {"question": "The ggplot2 is a graphics framework based on a layer grammar of graphics.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "In the graph theory, a cycle is a path that starts and ends at the same vertex.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "The number of edges of the graph is two. [Picture1.png]",
     "options": ["True", "False"], "answer": [2], "is_multiple": False, "image": "Picture1.png"},
    {"question": "The outcome of the expression below is FALSE\n2^4-1 >15",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "In a graph database relationships are represented by edges between vertices.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},

    # Q16–Q20
    {"question": "The outcome of the if below is TRUE\nIf(is.na(c(78,NA,56)[1]))",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "The output of the function below is 2\nwhich.min(c(78,56,88,93))",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "The loop below will iterate indefinitely\nRepeat(cat(‘hello’))",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "R is a compiler-based scripting language.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "The loop below will iterate five times\nfor(i in -2:3) ()",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},

    # Q21–Q25
    {"question": "In R a dataframe is a set of vectors of different data types",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "A dataset is said to be tidy if each variable has its own column and each observation has its own row.",
     "options": ["True", "False"], "answer": [1], "is_multiple": False},
    {"question": "In R a matrix is a one-dimensional array that has elements of the same data type.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "In R the next statement forces an exit from the body of a loop.",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},
    {"question": "The out-degree of the ‘Michael’ vertex shown below is two [Picture2.png]",
     "options": ["True", "False"], "answer": [1], "is_multiple": False, "image": "Picture2.png"},

    # Q26–Q30
    {"question": "The dpylr function used to add a new variable to a table that is a function of existing variables is",
     "options": ["A) filter()", "B) mutate()", "C) select()"], "answer": [2], "is_multiple": False},
    {"question": "The loop below will iterate ____.\nI <- 8; while(i >5) (i <- i-2)",
     "options": ["A) One time", "B) two times", "C) three times"], "answer": [2], "is_multiple": False},
    {"question": "The degree of the node below is [Picture3.png]",
     "options": ["A) One", "B) Two", "C) Three"], "answer": [2], "is_multiple": False, "image": "Picture3.png"},
    {"question": "The output of the code below is\nResult <- function(n=99) { \nreturn(n%%2) }\ncat(result()^99)",
     "options": ["A) 0", "B) 1", "C) 99"], "answer": [2], "is_multiple": False},
    {"question": "The loop below will iterate\ni <- 12\nrepeat(\n    i <- i-4\n    if(i < 3) {break})",
     "options": ["A) one times", "B) two times", "C) three times"], "answer": [3], "is_multiple": False},

    # Q31–Q35
    {"question": "The three hex values below will generate the following colours.\n#000000, #00FF00 , #FFFFFF",
     "options": ["A) Black, Green, White", "B) White, Green, Black", "C) Red, Green, Blue"], "answer": [1], "is_multiple": False},
    {"question": "[Picture4.png]",
     "options": ["A) plot(graph_from_literal(a:b+--c))",
                 "B) plot(graph_from_literal(a:b+--+c))",
                 "C) plot(graph_from_literal(a:b--+c))"], "answer": [3], "is_multiple": False, "image": "Picture4.png"},
    {"question": "The output of the code below is \nA <- matrix(1:6, nrow=2, ncol=3)\nfor(i in 1:nrow(A)){for(j in 1:ncol(A)) {cat(A[i,j])}}",
     "options": ["A) 135246", "B) 123456", "C) 246135"], "answer": [1], "is_multiple": False},
    {"question": "In ggplot2 the function used to draw a regression line in a scatter plot is",
     "options": ["A) geom_smooth()", "B) geom_point()", "C) geom_line()"], "answer": [1], "is_multiple": False},
    {"question": "The loop below will iterate ___ times\ng<-c(78,56,93,NA,89)\nfor (i in 1:length(g)) {\n    if(is.na(g[i])) {break}}",
     "options": ["A) Two", "B) three", "C) four"], "answer": [3], "is_multiple": False},

    # Q36–Q40
    {"question": "The outcome of the function below is \nmedian(0:5)",
     "options": ["A) 2", "B) 2.5", "C) 3"], "answer": [2], "is_multiple": False},
    {"question": "In ggplot2 the function that requires the x axis to be a categorical variable is",
     "options": ["A) geom_histogram()", "B) geom_bar()", "C) geom_freqpoly()"], "answer": [2], "is_multiple": False},
    {"question": "In a graph network a___ is a path that starts and ends at the same vertex",
     "options": ["A) cycle", "B) path", "C) loop"], "answer": [1], "is_multiple": False},
    {"question": "A_____ in R is made of vectors having different data types",
     "options": ["A) matrix", "B) data frame", "C) list"], "answer": [2], "is_multiple": False},
    {"question": "The R data type used to enable an object to store a Boolean value is",
     "options": ["A) Integer", "B) numeric", "C) logical"], "answer": [3], "is_multiple": False},

    # Q41–Q50
    {"question": "The dplyr function that reduces multiple values down to a single summary is",
     "options": ["A) filter()", "B) summarise()", "C) mutate()"], "answer": [2], "is_multiple": False},

    {"question": "The degree of node c in the graph network below is [Picture5.png]",
     "options": ["A) 2", "B) 3", "C) 4"], "answer": [3], "is_multiple": False, "image": "Picture5.png"},

    {"question": "In R the data structure we should use to store a one-dimensional array is a",
     "options": ["A) Matrix", "B) data frame", "C) vector"], "answer": [3], "is_multiple": False},

    {"question": "Which of the following squares negative 4 and adds 2 to the result?",
     "options": ["A) (-4)^2+2", "B) -4^2+2", "C) (-4)^(2+2)", "D) -4^2(2+2)"], "answer": [1], "is_multiple": False},

    {"question": "In R the function used to categorize data is",
     "options": ["A) factor()", "B) cat()", "C) categorize()"], "answer": [1], "is_multiple": False},

    {"question": "In Tidyverse framework the package responsible for manipulating and filtering data is",
     "options": ["A) dplyr", "B) tibble", "C) readr"], "answer": [1], "is_multiple": False},

    {"question": "The output of the code below is\nn <- 1:4\nresult <- ifelse(n%% 2==1, ‘odd’, ‘even’)\ncat(result)",
     "options": ["A) odd even odd even", "B) even odd even odd", "C) odd even odd odd"], "answer": [1], "is_multiple": False},

    {"question": "Consider the code below\nv1<- c(2,1,1,3,2,1,0)\nv2<-c(3,8,2,2,0,0,0)\nif(v1[1]>=2 && v2[7] >v1[7]) {cat(‘Hello’)}",
     "options": ["True", "False"], "answer": [2], "is_multiple": False},

    {"question": "The output of the code below is\nc<-0\ncat(switch(c, ’red’, ’green’, ’blue’))",
     "options": ["A) red", "B) green", "C) blue", "D) No output"], "answer": [4], "is_multiple": False},

    {"question": "The output of the code below is \nn i <- factorial(4)\nrepeat {\n  i<-i-2^3\n  if(i<15) {break}\n}\ncat(i)",
     "options": ["A) 8", "B) 16", "C) 32"], "answer": [1], "is_multiple": False}
]
