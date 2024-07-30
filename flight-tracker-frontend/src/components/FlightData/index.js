import React, { useState } from "react";
import styles from "./styles.module.css";
import Icon from "@/images/DownArrow";

const extractTime = (dateString) =>
  new Date(dateString).toTimeString().slice(0, 5);

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const options = { weekday: "short", day: "2-digit", month: "long" };
  const parts = date.toLocaleDateString("en-GB", options).split(" ");
  return `${parts[0]}, ${parts[1]} ${parts[2]}`;
};

const COLOR_MAPPING = {
  Scheduled: "#6ab586",
  Delayed: "#ec9b0f",
  Cancelled: "red",
  Arrived: "#6ab586",
};

function FlightData({ data = {} }) {
  const [show, setShow] = useState(false);

  const handleClick = (e) => {
    e.preventDefault();
    setShow((pv) => !pv);
  };
  console.log(data);
  return (
    <div className={styles.body}>
      <div className={styles.container}>
        <div className={styles.status} style={{ marginRight: "40px" }}>
          {data.route ? data.route : "Direct"}
        </div>
        <div
          style={{
            display: "flex",
            flex: "1",
            flexDirection: "column",
            marginLeft: "50px",
          }}
        >
          <div
            style={{
              display: "flex",
              flex: "1",
              alignItems: "center",
              justifyContent: "space-between",
              backgroundColor: show ? COLOR_MAPPING[data.status] : "",
              color: show ? "#fff" : "",
              padding: "20px",
              borderRadius: "2px",
              transition: "0.4s ease-in-out",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "4px",
              }}
            >
              <div className={styles.city_name}>{data.origin_code_iata}</div>
              <div className={styles.flightInfo}>
                <div
                  className={`${styles.dot} ${
                    !show
                      ? styles[`${data.status.toLowerCase()}_dot`]
                      : styles["g_bg"]
                  }`}
                ></div>
                <div
                  className={`${styles.line} ${
                    !show ? styles[data.status.toLowerCase()] : styles["g_bg"]
                  }`}
                ></div>
                <div
                  className={`${styles.dot} ${
                    !show
                      ? styles[`${data.status.toLowerCase()}_dot`]
                      : styles.g_bg
                  }`}
                ></div>
              </div>
              <div className={styles.city_name}>
                {data.destination_code_iata}
              </div>
            </div>
            <div className={styles.text}>{data.ident_iata}</div>
            <div className={styles.text}>{extractTime(data.scheduled_on)}</div>
            <div className={styles.text}>{extractTime(data.estimated_on)}</div>
            <div
              className={`${styles.status} ${
                !show ? styles[`${data.status.toLowerCase()}_bg`] : styles.bgg
              }  `}
            >
              {data.status === "Scheduled" ? "On Time" : data.status}
            </div>
            <button
              onClick={handleClick}
              style={{
                all: "unset",
                cursor: "pointer",
                transform: show ? "rotate(180deg)" : "",
                transition: "1s linear ease-in-out",
              }}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="30"
                height="20"
                fill={show ? "#fff" : "#000"}
                version="1.1"
                viewBox="0 0 330 330"
                xmlSpace="preserve"
              >
                <g>
                  <path d="M325.607 79.393c-5.857-5.857-15.355-5.858-21.213.001l-139.39 139.393L25.607 79.393c-5.857-5.857-15.355-5.858-21.213.001-5.858 5.858-5.858 15.355 0 21.213l150.004 150a14.999 14.999 0 0021.212-.001l149.996-150c5.859-5.857 5.859-15.355.001-21.213z"></path>
                </g>
              </svg>{" "}
            </button>
          </div>

          <div
            style={{
              border: "1px solid #dedede",
              borderTop: "0px",
              padding: "16px",
              display: !show ? "none" : "",
              transition: "1s ease-in-out",
            }}
          >
            <div
              style={{ display: "flex", flexDirection: "column", gap: "16px" }}
            >
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    alignItems: "flex-end",
                    justifyContent: "space-between",
                    margin: "20px 0px",
                    gap: "10px",
                  }}
                >
                  <div className={styles.iata}>{data.origin_code_iata}</div>
                  <div>({data.origin_city})</div>
                </div>
                <div
                  className={`${
                    show
                      ? styles[`${data.status.toLowerCase()}_bg`]
                      : styles.bgg
                  } ${styles.status} `}
                >
                  {data.status === "Scheduled" ? "On Time" : data.status}
                </div>

                <div
                  style={{
                    display: "flex",
                    alignItems: "flex-end",
                    justifyContent: "space-between",
                    gap: "8px",
                  }}
                >
                  <div>({data.destination_city})</div>
                  <div className={styles.iata}>
                    {" "}
                    {data.destination_code_iata}
                  </div>
                </div>
              </div>
              <div>
                <div className={styles.flightInfo}>
                  <div
                    className={`${styles.dot} ${
                      styles[`${data.status.toLowerCase()}_dot`]
                    }`}
                  ></div>
                  <div
                    className={`${styles.line} ${
                      styles[data.status.toLowerCase()]
                    }`}
                  ></div>
                  <div
                    className={`${styles.dot} ${
                      styles[`${data.status.toLowerCase()}_dot`]
                    }`}
                  ></div>
                </div>
              </div>
              <div
                style={{
                  display: "flex",
                  alignItems: "flex-end",
                  justifyContent: "space-between",
                }}
              >
                <div>
                  <div>{formatDate(data.estimated_out)}</div>
                  <div>
                    Estimated Departure -{" "}
                    <span
                      style={{
                        color: COLOR_MAPPING[data.status],
                        fontSize: "22px",
                      }}
                    >
                      {extractTime(data.estimated_out)}{" "}
                    </span>{" "}
                    Scheduled Departure -{" "}
                    <span
                      style={{
                        color: COLOR_MAPPING[data.status],
                        fontSize: "22px",
                      }}
                    >
                      {extractTime(data.scheduled_out)}{" "}
                    </span>
                  </div>
                </div>

                <div>
                  <div>{formatDate(data.scheduled_on)}</div>
                  <div>
                    Estimated Arrival -{" "}
                    <span
                      style={{
                        color: COLOR_MAPPING[data.status],
                        fontSize: "22px",
                      }}
                    >
                      {extractTime(data.estimated_on)}{" "}
                    </span>
                    {"  "}Scheduled Arrival -{" "}
                    <span
                      style={{
                        color: COLOR_MAPPING[data.status],
                        fontSize: "22px",
                      }}
                    >
                      {extractTime(data.scheduled_on)}{" "}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FlightData;
