# vivekdemo2
just an demo
import "./App.css";
import Navbar from "./components/Navbar";
import Header from "./components/Header";
import About from "./components/About";
import Skills from "./components/Skills"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Projects from "./components/Projects";
import Contact from "./components/Contact";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route exact path="/">
            <Header/>
            <About/>
            <Skills/>
            <Projects />
            <Contact/>
          </Route>
          <Route path="/about" component={About}/>
          <Route path="/skills" component={Skills}/>
          <Route path="/projects" component={Projects}/>
          <Route path="/contact" component={Contact}/>
        </Switch>
      </Router>
    </>
  );
}

export default App;
