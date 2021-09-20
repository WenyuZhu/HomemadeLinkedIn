[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h1 align="center">Homemade LinkedIn</h1>

  <p align="center">
    A homemade LinkedIn backend project that can save users' info into a database.
    <br />
    <a href="https://github.com/WenyuZhu/HomemadeLinkedIn"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/WenyuZhu/HomemadeLinkedIn/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project uses a RESTful service [FastAPI](https://fastapi.tiangolo.com) to develop a backend application. It that can store users' info into or read it from a database, such as education history, work experience, etc. Besides the CRUD operations, the security functions are also developed, including login with passwords then verify it with the hashed password and authenticate users with encoded token.

### Built With

* [FastAPI](https://fastapi.tiangolo.com)
* [Unicorn](https://www.uvicorn.org/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* requirements.txt
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/WenyuZhu/HomemadeLinkedIn.git
   ```
2. Navigate to folder HomemadeLinkedIn
3. Run the server
   ```cmd
   unicorn app.main:app --reload
   ```
4. Go to http://127.0.0.1:8000/docs in a browser.


<!-- USAGE EXAMPLES -->
## Usage

1. Before you can sign in, please create an account(an user), find the 'Create User' button under 'defualt' tag, then click try it out, input your info in the request body field and hit the 'execute' button. 
2. [![CreateUser.PNG]]
3. Now you can sign in to the server. Find the 'Authorize' button on the top right corner, then input your email address in the 'username' field and the password.
4. After you signing in the server, you can do the read and save operation to the server.

_For more examples, please refer to the [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)_



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Wenyu Zhu - [@LinkedIn](https://www.linkedin.com/in/wenyu-zhu-059856b7) - wzz0015@auburn.edu

Project Link: [https://github.com/WenyuZhu/HomemadeLinkedIn](https://github.com/WenyuZhu/HomemadeLinkedIn)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [FastAPI](https://fastapi.tiangolo.com/)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/WenyuZhu/HomemadeLinkedIn?style=flat-square
[contributors-url]: https://github.com/WenyuZhu/HomemadeLinkedIn/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/WenyuZhu/HomemadeLinkedIn?style=flat-square
[forks-url]: https://github.com/WenyuZhu/HomemadeLinkedIn/network/members
[stars-shield]: https://img.shields.io/github/stars/WenyuZhu/HomemadeLinkedIn?style=flat-square
[stars-url]: https://github.com/WenyuZhu/HomemadeLinkedIn/stargazers
[issues-shield]: 	https://img.shields.io/github/issues/WenyuZhu/HomemadeLinkedIn?style=flat-square
[issues-url]: https://github.com/WenyuZhu/HomemadeLinkedIn/issues
[license-shield]: https://img.shields.io/github/license/WenyuZhu/HomemadeLinkedIn?style=flat-square
[license-url]: https://github.com/WenyuZhu/HomemadeLinkedIn/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/wenyu-zhu-059856b7/
[product-screenshot]: images/screenshot.png
