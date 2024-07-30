import React from "react";
import styles from "@/styles/Home.module.css";
import Head from "next/head";
import { Inter } from "next/font/google";
import useFetchFlightDetails from "@/hooks/useFetchFlightDetails";
import SearchBox from "@/components/SearchBox";
import FlightData from "@/components/FlightData";
import { useRouter } from "next/router";

const inter = Inter({ subsets: ["latin"] });

function index() {
  const router = useRouter();

  const { flightData = [] } = useFetchFlightDetails();

  const handleBack = (e) => {
    e.preventDefault();
    router.push("/");
  };

  return (
    <>
      <Head>
        <title>Flight Tracker App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={`${styles.main} ${inter.className}`}>
        <button
          onClick={handleBack}
          style={{ all: "unset", cursor: "pointer", padding: "20px" }}
        >
          {" "}
          <u> Go Back</u>
        </button>
        {(flightData || []).length ? (
          <div className={styles.body}>
            {(flightData || []).map((it) => (
              <FlightData key={it.id} data={it} />
            ))}
          </div>
        ) : (
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: "40px",
              height: "80%",
            }}
          >
            {" "}
            Uh Oh, No Data Found!!!
          </div>
        )}
      </div>
    </>
  );
}

export default index;