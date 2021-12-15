import { Grid } from "@mui/material";
import Leftbar from "./components/leftbar/Leftbar";
import Navbar from "./components/navbar/Navbar";
import Homepage from "./pages/homepage";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Userpage from "./pages/userpage";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Grid container>
          <Grid item sm={2}>
            <Leftbar></Leftbar>
          </Grid>
          <Grid item sm={10}>
            <Routes>
              <Route path="/" element={<Homepage />} />
              <Route path="/users" element={<Userpage />} />
            </Routes>
          </Grid>
        </Grid>
      </BrowserRouter>
    </div>
  );
}

export default App;
