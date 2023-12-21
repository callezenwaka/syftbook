// handle site constants
const LANGUAGE = 'en';
const VERSION = 'latest';
const YEAR = new Date().getFullYear();

// handle window location and url
const { origin, pathname } = location;
const { host, hostname, port } = new URL(origin);
const ENV = ['localhost', '127.0.0.1'].includes(hostname)? `dev` : `prod`;
const SITE_URL = ENV === 'prod'? `${origin}/${LANGUAGE}/${VERSION}` : `http://${host}`;
// const env = hostname === 'syftbook.readthedocs.io'? `prod` : `dev`;
// const SITE_URL = hostname === ('localhost' || '127.0.0.1')? `http://${host}/docs/_build/html`: `${origin}/en/latest`;

function buildNavigation() {
  // build the href for the navigation tabs
  const nodeList = document.querySelectorAll(".nav-item .nav-link.nav-internal");
  const links = Array.from(nodeList);

  // map href links
  links.map( link => {
    const { href } = link;
    var { pathname } = new URL(href);
    link.setAttribute("href", SITE_URL + pathname);
    return link;
  });

};

document.addEventListener("locationchange", buildNavigation);


document.addEventListener("DOMContentLoaded", buildNavigation);