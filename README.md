# Book-Recommendation-System
Analytics Edge Project


\documentclass[utf8]{article}
\usepackage[utf8]{inputenc}
\setlength{\parindent}{0pt}
\usepackage{geometry}
\usepackage{multirow}
\geometry{a4paper, portrait, margin=0.55in}
\usepackage{graphicx}
\graphicspath{ {./Images/} }
\usepackage{float}
\usepackage{tabularx}
\usepackage[compact]{titlesec}
\title{%
Personalized Book Recommendation System}
\author{Rachit Jain, Bibhabasu Das, Shreya Gupta, Abhranil Chakrabarti}
\date{December 2022}

\begin{document}
\maketitle
\section{Overview}
In this digital era, most industries have seen a major shift towards using digital platforms to push their offerings, with a sharp rise in user traction during the COVID-19 pandemic. User experience is key on such platforms and a smart equivalent of a traditional salesperson becomes increasingly essential. This is where recommendation systems come into the picture. They understand user behavior and their requirements to recommend them the offerings/products that are most relevant to them, and hence are most likely to buy. Some of the major e-commerce players in the industry, like Amazon, have figured out how to create the best recommendation system, that keeps improving with time, owing to increased information availability for each user. The purpose of this project is to explore recommendation methods on a specific application, that can be easily extended to any domain, displaying the power and relative ease of implementation of such methods.

\maketitle
\section{Objective and Scope}
This project aims to build a recommendation system that uses historical book rating information available for users to recommend books to them. The key idea behind a recommendation system is that users who share similar preferences are most probable to like similar items; users who like an item are probable to like a similar item.

\maketitle
\section{Data Used}
We rely on data retrieved from multiple data sources to get information on books, ISBN, author, review, and corresponding reviewer information. The following data sources are used:
\begin{itemize}
    \item Amazon Data: 51.3M reviews and 2.9M products
    \begin{itemize}
        \item \textbf{Sample Review:} ReviewerID, ProductID, Review, Overall Rating, Review Date, etc. 
        \item \textbf{Meta Data:} ProductID, Title, Price, Also Bought, Also Viewed, Bought Together, Category, etc.   
    \end{itemize}
    \item \textbf{Kaggle Data:} 271k books, 279k Users, 1.1M Reviews 
    \begin{itemize}
        \item \textbf{Book Data Labels:}ISBN, Book-Title, Book-Author, Publisher, Year-of-Publication, Image-URL 
        \item \textbf{Rating Data Labels: }UserID, ISBN, Rating; User Data: User-ID, Location, Age
    \end{itemize}
\end{itemize}

\maketitle
\section{Data Cleaning \& Preprocessing}
We use Kaggle data as our base and extract information from Amazon dataset to enhance the models to be built. We perform the following data cleaning steps:
\begin{itemize}
    \item \textbf{Filtering data: }Since the user-book rating information is very sparse (i.e., ratings available for a very small subset of books for each user), we limit our recommendation system to rely on information for users who have rated at least 200 books and for books that have at least 50 ratings. This makes the ratings as well as the users more “reliable”.
    \item \textbf{Extracting book meta-data:  }The Kaggle dataset does not contain enough information about books to get a reliable understanding of user preferences. So, we extract additional data on books like ‘Description’, ‘Price’ and ‘Category’. We also get data on behavior of users who bought those books, like ‘Also Bought’ and ‘Also Viewed’.
\end{itemize}


\maketitle
\section{Understanding the Data}
The following charts indicate how the data is distributed. In Figure 1, we can see that the 3 most frequently rated authors are Agatha Christie, William Shakespeare and Stephen King. This is not surprising as these are some of the most widely known authors. \\
The distribution of ratings indicates that people generally rate a book only if they moderately liked it or really liked it. Very few users bother to rate books if they completely disliked it. 
\flushbottom
\maketitle
\thispagestyle{empty}

\begin{figure}[!htb]
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.7]{Images/Picture1a.png}
     \caption{Most Frequently Rated Authors}\label{Fig:Data1}
   \end{minipage}\hfill
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.7]{Images/Picture1b.png}
     \caption{Distribution of Ratings}\label{Fig:Data2}
   \end{minipage}
\end{figure}

\maketitle
\section{Recommendation Approach}
The system makes different recommendations based on the kind of user.
\begin{itemize}
    \item \textbf{New User}: For a new user, we recommend the most popular book in general or within a specified genre. This is because we have no data on the user to determine the user's preferences. In a real-time system, the system would recognize this as a new user, and start tracking information for them to be able to make better and more relevant recommendations in the future.
    \item \textbf{Existing User:} Since we already have the ratings for some books in our data, we rely on this information to provide book recommendations (both at an overall and at a genre level)
\end{itemize}

\

\textbf{Similarity Measure}
As the name suggests, similarity measures indicate how "similar" or "close" two users or two items are to each other. One of the most common similarity measures is \textbf{"cosine similarity"}, generated by mapping features available for the user/item in a latent space.

\

We use some of the most widely applied methodologies for recommendation systems and compare the results obtained from each.\

\begin{itemize} 
\item \textbf{Naïve Recommendation:} Recommend the most popular book for new users, i.e., rank books by their ratings and then recommend
\item \textbf{Content Based Recommendations System:} Build models that rely on user and book attributes as inputs to predict ratings. Key techniques used: Linear Regression, Holistic Regression, XGBoost \
\begin{figure}[H]
\begin{center}
\includegraphics[scale=0.7]{Images/Picture4.png}
\caption{Content-based Filtering Method}
\label{content_based}
\end{center}
\end{figure}
\item \textbf{Collaborative Filtering:} The dataset used for recommendation systems is generally very sparse (has a lot of blanks). This is because we have information available for very few items for each user. Collaborative filtering deals with this sparsity by decomposing the data lower dimensional matrices that represent the users and items (in a latent space). The key idea is that people who agreed in their evaluation of certain items are likely to agree again in the future. 
\item \textbf{Hybrid Methods:} Collective matrix factorization to combine user-item ratings with book and user attributes to give more informed recommendations



\end{itemize}

\maketitle
\section{Optimization for Recommendation}

For recommendations to a particular user, we solve the following optimization problem to account for the liking of the user along with the variety of the recommended book set

\textbf{Variables:}

\begin{itemize}
    \item $R_i$ - Predicted rating of book i by the chosen user
    \item $B_i$ - Feature vector of book i
    \item $X_i$ - Decision Variable: 1 if book i is recommended and 0 otherwise
    \item $Y_{ij}$ - Decision Variable: 1 if book i and book j are both in the recommended list and 0 otherwise
\end{itemize}

\textbf{Objective:} \\

\begin{center}
    $ max_{X} \sum_i X_i * R_i $
\end{center}

\textbf{Constraints:}

\begin{itemize}
    \item We must recommend K books (K=5 in our case): 
    
    $\sum_i X_i = K $
    
    \item Recommended books must not be very similar ($\rho=0.6$ in our case):
    
    $ Y_{ij} * \frac{B_i^T B_j}{|B_i||B_j|} <= \rho, \forall i,j$

    \item Linking Constraints: 

    $ Y_{ij} >= X_i, Y_{ij} >= X_j  \forall i,j$

    \item Binary Decision Variables:

    $X_i \in \{0,1\}; Y_{ij} \in \{0,1\}$
    
\end{itemize}

We perform the optimization over the 100 most highly rated books of the user to make the problem more tractable




\maketitle
\section{Results}
We assess the performance of the models on the root mean squared error on the test set predictions. This is compared against a baseline whose predicted rating for a user-item pair is the average rating with added Gaussian noise. XGBoost and Collaborative Filtering (via SVD) perform the best on the test set, achieving a reduction of 35\% and 33\% over the baseline

\begin{figure}[H]
\begin{center}
\includegraphics[scale=0.25]{Images/Results.jpeg}
\caption{Test Set Results}
\label{53_rec}
\end{center}
\end{figure}

We also look at 2 users, looking at their ratings to understand their preferences and assess the recommendations provided to each of them
\\

\subsection{User 9512 (most number of ratings)}\label{user 1}
\begin{figure}[!htb]
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.5]{Images/9512_a.png}
     \caption{Most rated categories}\label{Fig:user9512a}
   \end{minipage}\hfill
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.5]{Images/9512_b.png}
     \caption{Distribution of Ratings}\label{Fig:user9512b}
   \end{minipage}
\end{figure}

\begin{figure}[H]
\begin{center}
\includegraphics[scale=0.4]{Images/Rec_9512.png}
\caption{Recommendations for User 9512 across different methods}
\label{9512_rec}
\end{center}
\end{figure}

\begin{itemize}
    \item User 9512 has mostly rated books in 'Literature \& Fiction', 'Mystery' and 'Science Fiction \& Fantasy' categories. The rating distribution indicates that the user rates only those books that they like (as all ratings are either 4 or 5).
    \item We see that XGBoost and Archetypal Clustering give the best results for this user, as the categories recommended by them are closest to the most rated categories by this user. 
    \item The optimization approach does recommend a diverse set of books while the Hybrid approach recommends books in categories which the user has not rated
\end{itemize}

\titlespacing{\section}{0}{0}{0}
\AtBeginDocument{
    \setlength\abovedisplayskip{0pt}
  \setlength\belowdisplayskip{0pt}}
  
\subsection{User 53 (randomly selected)}\label{user 2}

\begin{figure}[!htb]
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.5]{Images/53_a.png}
     \caption{Most rated categories}\label{Fig:user53a}
   \end{minipage}\hfill
   \begin{minipage}{0.48\textwidth}
     \centering
     \includegraphics[scale=0.5]{Images/53_b.png}
     \caption{Distribution of Ratings}\label{Fig:user53b}
   \end{minipage}
\end{figure}

\begin{figure}[H]
\begin{center}
\includegraphics[scale=0.5]{Images/Rec_53.png}
\caption{Recommendations for User 53 across different methods}
\label{53_rec}
\end{center}
\end{figure}

\begin{itemize}
    \item User 53 has very few ratings (225 ratings) in comparison to user 9512 (5617 ratings)
    \item User 53 has mostly rated books in 'Literature \& Fiction', 'Teen \& Young Adult' and 'Mystery' categories. The rating distribution indicates that the user rates books they liked as well as the ones they didn't like.
    \item We see that XGBoost and Archetypal Clustering give the best results for this user, as the categories recommended by them are closest to the most rated categories by this user.  
     \item SVD with optimization provides recommendations in newer categories for which the user has rated very few books (or none at all). Hybrid Filtering recommends all books in the same category ('Children's books), which despite having a few books rated by the user, might not be the best recommendation (no diversification and not a good representation of user rating behavior).
\end{itemize}

\\

\maketitle
\section{Impact}
This project is an implementation of some of the most widely used recommendation practices across industries, and can be extend to the following applications:
\begin{itemize}
    \item The recommendation system can be used by a marketplace as a part of its push strategy to understand
    its users, recommend them books while also deciding price point of these books dynamically (based on
    trending prices in the book category and user willingness to pay historically).
    \item This system is agnostic to product category and can be embedded as a part of customer experience improvement for any platform, thereby empowering the customer with reliable and personalized information
\end{itemize}



\bibliography{sample}

\end{document}
