import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";

import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import Navigation from "./components/Navigation";
import LandingPage from "./components/LandingPage";
import PinsList from "./components/Pins/PinsList/PinsList";
import SinglePinDetails from "./components/Pins/SinglePinDetails/SinglePinDetails";
import CreatePin from "./components/Pins/CreatePin/CreatePin";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      <div>
        {isLoaded && (
          <Switch>
            <Route exact path="/">
              <LandingPage />
            </Route>
            <Route exact path="/login">
              <LoginFormPage />
            </Route>
            <Route exact path="/signup">
              <SignupFormPage />
            </Route>
            <Route exact path="/pins">
              <PinsList />
            </Route>
            <Route exact path="/pins/:pinId">
              <SinglePinDetails />
            </Route>
            <Route exact path="/pin-builder">
              <CreatePin />
            </Route>
            <Route exact path="/:username/board-builder">
              <CreatePin />
            </Route>
          </Switch>
        )}
      </div>
    </>
  );
}

export default App;
