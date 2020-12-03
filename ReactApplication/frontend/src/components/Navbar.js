import React from "react";
import {
  Navbar,
  Nav,
  Form,
  FormControl,
  Button,
  Container,
  Col
} from "react-bootstrap";
import "./navbar.css";

class NavBar extends React.Component {
  render() {
    const { toggle } = this.props;

    return (
      <>
        <Navbar
          expand="xl"
          className="color-nav"
          variant="light"
          fixed="top"
          collapseOnSelect
        >
          <Container fluid>
            <Navbar.Brand href="#home"  bsPrefix="heading">
              HealthScroll            
              </Navbar.Brand>

            <Navbar.Toggle
              className="ml-3 mb-2"
              aria-controls="responsive-navbar-nav"
              onClick={toggle}
            />
            <Navbar.Collapse id="basic-navbar-nav">
              <Col>
                <Nav.Item>
                  <Form inline>
                    <FormControl
                      type="text"
                      placeholder="Search For Medicines"
                      className="mr-sm-6 m-1"
                      size="lg"
                    />
                    <Button className="m-1" variant="outline-info" size="lg">
                      Search
                    </Button>
                  </Form>
                </Nav.Item>
              </Col>
              <Col md="auto">
                <Button className="m-1" variant="primary" size="lg">
                  Wellness Blogs
                </Button>
                <Button className="m-1" variant="primary" size="lg">
                  Latest News
                </Button>
                <Button className="m-1" variant="primary" size="lg">
                  About
                </Button>
              </Col>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </>
    );
  }
}
export default NavBar;
