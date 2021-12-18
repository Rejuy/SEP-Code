import { Card, Typography, styled } from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import {
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import "../../config";

const CustomCard = styled(Card)(({ theme }) => ({
  width: "100%",
  padding: theme.spacing(2),
}));

export default function UserChangePlot() {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios
      .get(global.config.backendUrl + "/api/admin/get_user_change_monthly")
      .then((res) => {
        var monthlyData = [];
        const resData = res.data.change;
        resData.forEach(function (item, index) {
          monthlyData.push({ month: index, change: item });
        });
        setData(monthlyData);
      });
  }, []);
  return (
    <CustomCard style={{ width: "100%" }}>
      <Typography variant="h6" component="div" style={{ marginBottom: "20px" }}>
        User Analytics: User Change
      </Typography>
      <ResponsiveContainer width="100%" aspect={4 / 1}>
        <LineChart data={data}>
          <XAxis dataKey="month" />
          <YAxis dataKey="change" />
          <Line type="monotone" dataKey="change" />
          <Tooltip
            labelFormatter={(l) => {
              const months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
              ];
              return months[l];
            }}
          ></Tooltip>
        </LineChart>
      </ResponsiveContainer>
    </CustomCard>
  );
}
