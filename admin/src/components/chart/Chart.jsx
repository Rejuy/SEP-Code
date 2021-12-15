import { Card, Typography, styled } from "@mui/material";
import React from "react";
import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis } from "recharts";

const CustomCard = styled(Card)(({ theme }) => ({
  width: "100%",
  padding: theme.spacing(2),
}));

export default function Chart() {
  const data = [
    {
      name: "Page A",
      uv: 4000,
      pv: 2400,
      amt: 2400,
    },
    {
      name: "Page B",
      uv: 3000,
      pv: 1398,
      amt: 2210,
    },
    {
      name: "Page C",
      uv: 2000,
      pv: 9800,
      amt: 2290,
    },
    {
      name: "Page D",
      uv: 2780,
      pv: 3908,
      amt: 2000,
    },
    {
      name: "Page E",
      uv: 1890,
      pv: 4800,
      amt: 2181,
    },
    {
      name: "Page F",
      uv: 2390,
      pv: 3800,
      amt: 2500,
    },
    {
      name: "Page G",
      uv: 3490,
      pv: 4300,
      amt: 2100,
    },
  ];
  return (
    <CustomCard style={{ width: "100%" }}>
      <Typography variant="h6" component="div" style={{ marginBottom: "20px" }}>
        User Analytics
      </Typography>
      <ResponsiveContainer width="100%" aspect={4 / 1}>
        <LineChart data={data}>
          <XAxis dataKey="name" />
          <Line type="monotone" dataKey="uv" />
          <Tooltip></Tooltip>
        </LineChart>
      </ResponsiveContainer>
    </CustomCard>
  );
}
