import {
  Button,
  Card,
  CardActions,
  CardContent,
  Typography,
} from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Timeonline() {
  const [count, setCount] = useState(0);
  const [start, setStart] = useState(false);
  useEffect(() => {
    if (!start) {
      setStart(true);
      axios
        .get("http://localhost:5000/api/admin/get_online_time")
        .then((res) => {
          setCount((new Date() - new Date(res.data.date)) / 1000);
          setInterval(() => {
            setCount((prevCount) => prevCount + 1);
          }, 1000);
        });
    }
  }, [start, count]);
  return (
    <Card>
      <CardContent>
        <Typography variant="h6" component="div">
          Server Online Time
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          Since Last Boot
        </Typography>
        <div
          style={{
            display: "flex",
            alignItems: "baseline",
            justifyContent: "space-evenly",
          }}
        >
          <Typography sx={{ fontSize: 24 }} color="text.primary" gutterBottom>
            {Math.floor(count / 3600)} Days
          </Typography>
          <Typography sx={{ fontSize: 20 }} gutterBottom>
            {Math.floor((count / 60) % 60)} Minutes
          </Typography>
          <Typography sx={{ fontSize: 16 }} gutterBottom>
            {Math.floor(count % 60)} Seconds
          </Typography>
        </div>
      </CardContent>
      <CardActions>
        <Link to="/analytics">
          <Button size="small">Learn More</Button>
        </Link>
      </CardActions>
    </Card>
  );
}
