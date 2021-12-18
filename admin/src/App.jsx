import { Grid } from "@mui/material";
import Leftbar from "./components/leftbar/Leftbar";
import Navbar from "./components/navbar/Navbar";
import Homepage from "./pages/homepage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Userpage from "./pages/userpage";
import Coursepage from "./pages/coursepage";
import Userinfo from "./pages/userinfo";
import Analytics from "./pages/analytics";
import Login from "./pages/login";
import RequireAuth from "./pages/requireAuth";

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
                      <Route path="/courses" element={<Coursepage />} />
                      <Route path="/user/:uid" element={<Userinfo />} />
                      <Route path="/analytics" element={<Analytics />} />
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
