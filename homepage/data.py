def get_education_background():
    x1 = {
    'imgurl' : 'homepage/img/images/cornell1.jpg',
    'schoolname' : 'Cornell University' ,
    'degreename' : 'Masters in Management',
    'duration' : 'August 2018 - May 2020',
    'courseslist' : ['Mathematical Programming','Econometrics','Applied Microeconomics','Stochastic Processes','Models and Methods for Causal Inference','Advanced Language Technologies (NLP)','Numerical Methods for Data Science']
    }
    x2 = {
    'imgurl' : 'homepage/img/images/iit5.jpg',
    'schoolname' :'Indian Institute of Technology Delhi' ,
    'degreename' : 'Bachelors in Computer Science' ,
    'duration' : 'August 2014 - May 2018',
    'courseslist' : ['Deep Learning','Machine Learning','Artificial Intelligence','Operating Systems','Computer Networks','Data Structures and Algorithms','Design and Analysis of Algorithms','Software Design Practices']
    }
    return [x1, x2]

def get_experience():
    x1 = {
    'imgurl' : 'homepage/img/job/kritikal-logo-2.png',
    'title' : 'Software Engineering Intern',
    'company' : 'Kritikal Solutions',
    'location' : 'Delhi, India',
    'url' : 'https://kritikalsolutions.com/',
    'duration' : 'December 2016',
    'description' : ['Developed a python program to inter-convert text between braille code language and other common languages for an electronic reader used by blind people']
    }
    x2 = {
    'imgurl' : 'homepage/img/job/microsoft-logo-2.png',
    'title' : 'Software Engineering Intern',
    'company' : 'Microsoft',
    'location' : 'Bengaluru, India',
    'url' : '',
    'duration' : 'May 2017 – July 2017',
    'description' : ['Built a web application in C# to enable multi-factor authentication to access azure cloud storage (ADLS) clusters using authorization code grant flow protocol']
    }
    x3 = {
    'imgurl' : 'homepage/img/job/amazon-logo-3.png',
    'title' : 'Software Engineer',
    'company' : 'Amazon Web Services',
    'location' : 'Seattle, Washington',
    'url' : '',
    'duration' : 'July 2020 - Present',
    'description' : ''
    }
    return [x3, x2, x1]


def get_ta_experience():
    x1 = {
    'title' : 'NBA 6420 - Supply Chain Analytics',
    'subtitle' : 'Prof. Li Chen',
    'location' : 'Cornell University',
    'url' : 'https://classes.cornell.edu/browse/roster/SP20/class/NBA/6420',
    'duration' : 'Mar 2020 – May 2020',
    'description' : []
    }
    x2 = {
    'title' : 'NBA 6430 - Managerial Spreadsheet Modeling',
    'subtitle' : 'Prof. Li Chen',
    'location' : 'Cornell University',
    'url' : 'https://classes.cornell.edu/browse/roster/SP20/class/NBA/6430',
    'duration' : 'Mar 2020 – May 2020',
    'description' : []
    }
    x3 = {
    'title' : 'NBA 6145 - AI Strategy and Applications',
    'subtitle' : 'Prof. Soumitra Dutta',
    'location' : 'Cornell University',
    'url' : 'https://classes.cornell.edu/browse/roster/FA19/class/NBA/6145',
    'duration' : 'Jun 2019 – Aug 2019',
    'description' : []
    }
    x4 = {
    'title' : 'NBA 6690 - Building a Consumer Internet Business',
    'subtitle' : 'Prof. Prashant Fuloria',
    'location' : 'Cornell University',
    'url' : 'https://classes.cornell.edu/browse/roster/SP19/class/NBA/6690',
    'duration' : 'Jan 2019 – Mar 2019',
    'description' : []
    }
    return [x1, x2, x3, x4]


def get_cornell_research():
    x1 = {
    'title' : 'Estimating Unbiased Ratings for Online Review Platforms',
    'subtitle' : 'Prof. Li Chen & Prof. Shawn Mankad',
    'location' : 'Cornell University',
    'url' : '',
    'duration' : 'Jan 2019 – May 2020',
    'description' : [
    'Identified role of elite Yelp users to reduce polarization bias in reviews',
    'Proposed and built ML models to predict unbiased ratings for businesses'
    ]
    }
    x2 = {
    'title' : 'Gender Debiasing in Pronoun Resolution Models',
    'subtitle' : 'CS6740 : Advanced Language Technologies',
    'location' : 'Cornell University',
    'url' : '',
    'duration' : 'Jan 2019 – May 2019',
    'description' : [
    'Implemented a recurrent neural network architecture for pronoun resolution',
    'Enhanced model performance by 5% & reduced gender bias from 8% to 0.2%'
    ]
    }
    x3 = {
    'title' : 'Predicting Friendship Links for Social Networks',
    'subtitle' : 'CS 6241: Numerical Methods for Data Science',
    'location' : '',
    'url' : '',
    'duration' : 'Jan 2019 – May 2019',
    'description' :['Implemented graph convolutional networks to predict friends on Yelp with 93.4% accuracy']
    }
    x4 = {
    'title' : ' Research Assistant',
    'subtitle' : 'Prof. Vrinda Kadiyali',
    'location' : 'Cornell University',
    'url' : '',
    'duration' : 'Jan 2020 – May 2020',
    'description' : []
    }
    return [x1, x2, x3, x4]


def get_iit_research():
    x1 = {
    'title' : 'Price Forecasting & Anomaly Detection for Agricultural Commodities',
    'subtitle' : 'Prof. Parag Singla & Prof. Aaditeshwar Seth',
    'location' : 'IIT Delhi',
    'url' : '',
    'duration' : 'Jan 2017 – March 2018',
    'description' : [
    ]
    }
    return [x1]


def get_timeline():
    kritikal = {
    'imgurl' : 'homepage/img/job/kritikal-logo-2.png',
    'title' : 'Software Engineering Intern',
    'company' : 'Kritikal Solutions',
    'location' : 'Delhi, India',
    'url' : 'https://kritikalsolutions.com/',
    'duration' : 'December 2016',
    'description' : ['Developed a python program to inter-convert text between braille code language and other common languages for an electronic reader used by blind people']
    }
    microsoft = {
    'imgurl' : 'homepage/img/job/microsoft-logo-2.png',
    'title' : 'Software Engineering Intern',
    'company' : 'Microsoft',
    'location' : 'Bengaluru, India',
    'url' : '',
    'duration' : 'May 2017 – July 2017',
    'description' : ['Built a web application in C# to enable multi-factor authentication to access azure cloud storage (ADLS) clusters using authorization code grant flow protocol']
    }
    amazon = {
    'imgurl' : 'homepage/img/job/amazon-logo-3.png',
    'title' : 'Software Engineer',
    'company' : 'Amazon Web Services',
    'location' : 'Seattle, Washington',
    'url' : '',
    'duration' : 'July 2020 - Present',
    'description' : ''
    }
    cornell = {
    'imgurl' : 'homepage/img/job/cornell-logo-1.png',
    'company' : 'Cornell University' ,
    'title' : 'Masters in Management',
    'location' : 'Ithaca, New York',
    'duration' : 'August 2018 - May 2020',
    'descriptioon' : ''
    }
    iit = {
    'imgurl' : 'homepage/img/job/iit-logo-1.png',
    'company' :'Indian Institute of Technology Delhi' ,
    'title' : 'Bachelors in Computer Science' ,
    'location' : 'New Delhi, India',
    'duration' : 'August 2014 - May 2018',
    'courseslist' : ''
    }
    return [amazon, cornell, iit, microsoft, kritikal]


def get_speaking_events():
    x1 = {
    'title' : 'Building Successful Tech Life',
    'venue' : 'Indian Institute of Technology Delhi',
    'date' : '8th Jan 2020',
    'staticimages' : [
    'homepage/img/events/1/a.jpg',
    'homepage/img/events/1/b.jpg'
    ],
    'description' : "We discussed that it is important to decide early on, the kind of career we want - so that we do not feel stuck doing something which we do not like - as it becomes increasingly difficult to switch careers in later stages. I emphasized how lifestyle - working hours, job environment - is as important as the work we do or the money we earn while choosing the career. Finally I shared my experiences and the interview process for big tech companies",
    'youtubelink' : "",
    'images' : []
    }
    x2 = {
    'title' : 'Indian Education System',
    'venue' : 'Youtube Channel : Yash Garg',
    'date' : '7th June 2020',
    'staticimages' : [],
    'description' : "I wanted to create this video for a long time to address issues such as suicides in Kota, suicides in IIT, why do students feel depressed even after cracking IIT, flaws in our education system and other relevant issues.",
    'youtubelink' : '9n20-61BK9Y',
    'images' : []
    }
    return [x2, x1]
