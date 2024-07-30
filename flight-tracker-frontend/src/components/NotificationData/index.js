import React from "react";
import styles from "./style.module.css";

const COLOR_MAPPING = {
  Scheduled: "#6ab586",
  Schedules: "#6ab586",
  Delayed: "#ec9b0f",
  Cancelled: "red",
  Arrived: "#6ab586",
};

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const options = { weekday: "short", day: "2-digit", month: "long" };
  const parts = date.toLocaleDateString("en-GB", options).split(" ");
  return `${parts[0]}, ${parts[1]} ${parts[2]}`;
};

const Card = ({ data }) => {
  const {
    id,
    departure_delay,
    arrival_delay,
    flight_name,
    status = "",
    scheduled_out,
  } = data;

  return (
    <div className={styles.body}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <h2 className={styles.h2}>Flight: {flight_name} </h2>
        <p>{formatDate(scheduled_out)}</p>
      </div>
      {id && (
        <>
          <span>Status</span>
          {":"}
          <span style={{ color: COLOR_MAPPING[status] }}> {status}</span>
        </>
      )}
      {departure_delay !== null && (
        <div>
          <span>Departure Delay:&nbsp;</span>
          <span style={{ color: COLOR_MAPPING[status] }}>
            {departure_delay} minutes
          </span>
        </div>
      )}
      {arrival_delay !== null && (
        <div>
          <span>Departure Delay:&nbsp;</span>
          <span style={{ color: COLOR_MAPPING[status] }}>
            {arrival_delay} minutes
          </span>
        </div>
      )}
    </div>
  );
};

export default Card;
