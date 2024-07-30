import React, { useState } from "react";
import styles from "./styles.module.css";
import { useRouter } from "next/router";

function SearchBox() {
  const router = useRouter();
  const [formVal, setFormval] = useState({
    departure: "",
    arrival: "",
    date: "",
    id: "",
    flight_id: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const filteredFormEntries = Object.entries(formVal).filter(
      ([key, val]) => val !== null && val !== ""
    );
    const queryParams = new URLSearchParams(filteredFormEntries).toString();
    router.push(`/search?${queryParams}`);
    console.log(formVal);
  };

  const handleChange = (e, val) => {
    setFormval((prevState) => ({
      ...prevState,
      [val]: e.target.value,
    }));
  };

  const button_disabled =
    formVal.flight_id ||
    (formVal.arrival && formVal.departure && formVal.date) ||
    formVal.id
      ? false
      : true;

  return (
    <div className={styles.body}>
      <div className={styles.inner_body}>
        <div className={styles.title}>Check Flight Status</div>

        <div>
          <form onSubmit={handleSubmit}>
            <div className={styles.form}>
              <div className={styles.form_element}>
                <input
                  value={formVal.departure}
                  onChange={(e) => {
                    handleChange(e, "departure");
                  }}
                  name="departure"
                  placeholder="Departure"
                />
                <div>Departure</div>
              </div>
              <div className={styles.form_element}>
                <input
                  value={formVal.arrival}
                  onChange={(e) => {
                    handleChange(e, "arrival");
                  }}
                  name="arrival"
                  placeholder="Arrival"
                />
                <div>Arrival</div>
              </div>
              <div className={styles.form_element}>
                <input
                  value={formVal.date}
                  onChange={(e) => {
                    handleChange(e, "date");
                  }}
                  name="date"
                  type="date"
                  placeholder="Date"
                />
                <div>Date of Travel</div>
              </div>
              <div className={styles.form_element}>
                <input
                  value={formVal.flight_number}
                  onChange={(e) => {
                    handleChange(e, "flight_number");
                  }}
                  placeholder="Flight Number"
                />
                <div>Flight Number</div>
              </div>
              <div className={styles.form_element}>
                <input
                  value={formVal.id}
                  onChange={(e) => {
                    handleChange(e, "id");
                  }}
                  placeholder="PNR"
                />
                <div>PNR</div>
              </div>
            </div>

            <button
              type="submit"
              disabled={button_disabled}
              onClick={handleSubmit}
              className={
                button_disabled ? styles.disabled_button : styles.button
              }
            >
              Search Flight
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SearchBox;
