<img src="https://img.shields.io/github/license/GabrielSantos198/ThunderStore?color=blue&style=for-the-badge" alt=""><img src="https://img.shields.io/github/repo-size/GabrielSantos198/ThunderStore?style=for-the-badge" alt=""><img src="https://img.shields.io/github/languages/count/GabrielSantos198/ThunderStore?style=for-the-badge" alt=""><img src="https://img.shields.io/github/issues/GabrielSantos198/ThunderStore?color=blue&style=for-the-badge" alt=""><img src="https://img.shields.io/github/issues-pr/GabrielSantos198/ThunderStore?color=blue&style=for-the-badge" alt=""><img src="https://img.shields.io/github/stars/GabrielSantos198/ThunderStore?color=blue&style=for-the-badge" alt="">

<p align="center">
<img src="static/imgs/logo.png" width=300px alt="">
</p>

<h1 align="center"> ⭐ Thunder Store </h1>

<p align="center">
  <sub> ⭐ This README covers all the specifics of the Thunder Store system.<sub>
</p>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#table-of-contents)

<p align="center">
  <a href="#introduction"> 🧩 Introduction </a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#results"> 🚀 Results</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#dependencies"> 🧪 Dependencies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#idea">💡 Possible Improvements</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#credits"> 🏆 Credits </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

<br/>

<a id="introduction"></a>
## 🧩 Introduction

  ***⠀⠀⠀⠀⭐ Thunder Store, an e-commerce project with safe, clean and open code for anyone who wants to use it. In the future I intend to use it to make my sales, for this reason I have often been implementing new features and improvements to the system.***

 ⭐ name | ⭐ technology
|---|---|
Front-End | <img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Html_fjsglo" alt=""><img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Css_qsq7eb" alt=""><img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Js_hm5nfd" alt=""><img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Bootstrap_h3arin" alt="">
Back-End | <img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Django_pvzwmf" alt=""><img src="https://res.cloudinary.com/degkn8uwg/image/upload/v1/media-portfolio/logo/Python_mqmv3x" alt="">
Others | Vim, Stripe, Docker, Google Analytics.
<br/>

<a id="results"></a>
## 🚀 Results
  > All results were successfully achieved. In general, these are the results of each request.

⭐ Name | ⭐ Link |
|---|---|
Home Page | https://thunderstore.up.railway.app/
Products Page | https://thunderstore.up.railway.app/produtos/
Featured Products | https://thunderstore.up.railway.app/#featured-products
About | https://thunderstore.up.railway.app/pagina/sobre/
Contact, Support | https://thunderstore.up.railway.app/pagina/contato/
Blog | https://thunderstore.up.railway.app/blog/
FaQ | https://thunderstore.up.railway.app/pagina/faqs/
Politic | https://thunderstore.up.railway.app/pagina/politica/
Track Order | https://thunderstore.up.railway.app/produto/rastreio/
Shopping Cart | https://thunderstore.up.railway.app/cart/cart-detail/
Login | https://thunderstore.up.railway.app/accounts/login/
Sign up | https://thunderstore.up.railway.app/accounts/signup/
<br/> 

## Screens

</summary>

### 🤳🏻 Mobile

<br />   


⭐ Home | ⭐ Product Detail | ⭐ Cart | ⭐ FaQ |
|---|---|---|---|
![Home](static/imgs/picture_1.png) | ![Product Detail](static/imgs/picture_2.png)| ![Cart](static/imgs/picture_3.png)| ![FaQ](static/imgs/picture_4.png)
  
  
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#table-of-contents)


### 💻 Desktop 
  
 ⭐ Home | ⭐ Product Detail | ⭐ Cart | FaQ |
|---|---|---|---|
![HomePage](static/imgs/picture_8.png) | ![Detalhes](static/imgs/picture_5.png) | ![Detalhes](static/imgs/picture_6.png) | ![Detalhes](static/imgs/picture_7.png)
<br/>
  
<a id="dependencies"></a>
## 🧪 Dependencies
> Requirements to rotate the code.
- Docker
- docker-compose

<h4>Step-1</h4> <code>git clone link https://github.com/GabrielSantos198/ThunderStore</code>

<h4>Step-2</h4> Change the values of environment variables in the docker-compose.yml.<br/><br/>

Key | Value
|---|---|
DEBUG | True/False
SECRET_KEY | Application secret key
EMAIL_HOST_USER | Your Gmail
EMAIL_HOST_PASSWORD | Gmail app password
RECIPIENT_ADDRESS | Message receipt email
CLOUD_NAME | Your name in Cloudinary
API_KEY | Your API key on Cloudinary
API_SECRET | Your API secret on Cloudinary
STRIPE_PUBLISHABLE_KEY | Your publishable key on Stripe
STRIPE_SECRET_KEY | Your secret key on Stripe
STRIPE_ENDPOINT_SECRET | Your Secret Endpoint on Stripe
<br />

OBS: <br/>
- Cloudinary is used to store media files.<br/>
- Stripe allows you to make payments in the system.<br/>
- I used a gmail app to receive e-commerce messages.<br/>

<h4>Step-3</h4> After placing the values of the environment variables, just run the command: <code>docker-compose up</code> and the application will be available on port 9000.<br/>
<br/>

OBS: It is also possible to run the application without docker, just clone the repository, create an .env file in the root of the project with the necessary keys and values ​​and install the project dependencies in requirements.txt, however the use of docker is encouraged, for a construction with no chance of failure.

<a id="idea"></a>
## 💡 Possible Improvements
> Possible code and design improvements if you want to go back and improve it.

<br />

  ### ***⠀⠀⠀⠀⭐ I believe that every project has things that can be improved, so here is an exclusive area for possible improvements or things that would be interesting to have in the project, but it will stay for the future.***


<br /> 

- [ ] ***- Test all code***
- [ ] ***- Add notification***
- [ ] ***- Add shipping calculator***
- [ ] ***- Add Change Password***


<br /> 

<a id="credits"></a>
## 🏆 Credits

  ### ***⭐ For every project we have to give credits to the creators so nothing better than finishing with a golden key with the creators / creator of the project***.

<br /> 

<div > 

| [<img src="https://avatars.githubusercontent.com/u/69887726?v=4" width=300><br><sub> Gabriel Santana </sub>](https://www.linkedin.com/in/gabrielsantana444) | ***Hello 😃 If you made it this far, I believe you liked my project, in which case we have something in common, so how about we talk a little? My call on linkedin*** 😁 |
|---|---|


</div> 
