import streamlit as st

def main():
    # Embedding CSS styles
    st.markdown("""
        <style>
            .title-row {
                color: white;
                text-align: center;
                background-color: #666362;
            }
            .page {
                color: white;
                background-color: #666362;
            }
            .site-footer {
                background-color: #26272b;
                padding: 45px 0 20px;
                font-size: 15px;
                line-height: 24px;
                color: #737373;
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            }
            .site-footer hr {
                border-top-color: #bbb;
                opacity: 0.5;
            }
            .site-footer hr.small {
                margin: 20px 0;
            }
            .site-footer h6 {
                color: #fff;
                font-size: 16px;
                text-transform: uppercase;
                margin-top: 5px;
                letter-spacing: 2px;
            }
            .site-footer a {
                color: #737373;
            }
            .site-footer a:hover {
                color: #fff;
                text-decoration: none;
            }
            .footer-author {
                padding-left: 0;
                list-style: none;
            }
            .footer-author li {
                display: block;
            }
            .footer-author a {
                color: #737373;
            }
            .footer-author a:active,
            .footer-author a:focus,
            .footer-author a:hover {
                color: #fff;
                text-decoration: none;
            }
            .copyright-text {
                margin: 0;
            }
            @media (max-width: 991px) {
                .site-footer [class^="col-"] {
                    margin-bottom: 30px;
                }
            }
            @media (max-width: 767px) {
                .site-footer {
                    padding-bottom: 0;
                }
                .site-footer .copyright-text,
                .site-footer .social-icons {
                    text-align: center;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Embedding HTML content
    st.markdown("""
        <html lang="en">
        <head>
            <meta charset="utf-8"/>
            <meta content="width=device-width, initial-scale=1.0" name="viewport">
            <title>Project</title>
            <link crossorigin="anonymous" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
                  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" rel="stylesheet">
            <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
                  integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA=="
                  rel="stylesheet"/>
            <link href="style.css" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="home.css">
        </head>
        <body>
        <!-- Your HTML content here -->
        </body>
        <footer class="site-footer">
            <div class="container">
                <div class="row">
                    <div class="col-6 col-md-3">
                        <h6>Author</h6>
                        <ul class="footer-author ">
                            <li>Name: Tianxin Yin (Stark)</li>
                            <li>Student ID: 1330365249</li>
                        </ul>
                    </div>
                    <hr class="small">
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 col-sm-6 col-12">
                            <p class="copyright-text">Copyright © 2022 All Rights Reserved</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        </html>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
