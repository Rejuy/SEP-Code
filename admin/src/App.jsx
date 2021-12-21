import { Grid } from "@mui/material";
import Leftbar from "./components/leftbar/Leftbar";
import Navbar from "./components/navbar/Navbar";
import Homepage from "./pages/homepage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Userpage from "./pages/userpage";
import Coursepage from "./pages/coursepage";
import Userinfo from "./pages/userinfo";
import Login from "./pages/login";
import RequireAuth from "./pages/requireAuth";
import Courseinfo from "./pages/courseinfo";
import Foodpage from "./pages/foodpage";
import NotFound from "./pages/notfoundpage";
import Foodinfo from "./pages/foodinfo";
import Placepage from "./pages/placepage";
import Placeinfo from "./pages/placeinfo";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/*"
            element={
              <RequireAuth>
                <Navbar />
                <Grid container>
                  <Grid item sm={2}>
                    <Leftbar></Leftbar>
                  </Grid>
                  <Grid item sm={10}>
                    <Routes>
                      <Route path="/" element={<Homepage />} />
                      <Route path="/users" element={<Userpage />} />
                      <Route path="/user/:uid" element={<Userinfo />} />
                      <Route path="/courses" element={<Coursepage />} />
                      <Route path="/course/:id" element={<Courseinfo />} />
                      <Route path="/foods" element={<Foodpage />} />
                      <Route path="/food/:id" element={<Foodinfo />} />
                      <Route path="/places" element={<Placepage />} />
                      <Route path="/place/:id" element={<Placeinfo />} />
                      <Route path="*" element={<NotFound />} />
                    </Routes>
                  </Grid>
                </Grid>
              </RequireAuth>
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
