---
type: Jurisdiction
title: "Muskogee County, OK"
classification: county
fips: "40101"
state: "OK"
demographics:
  population: 66444
  population_under_18: 16195
  population_18_64: 38803
  population_65_plus: 11446
  median_household_income: 53619
  poverty_rate: 19.12
  homeownership_rate: 66.52
  unemployment_rate: 5.66
  median_home_value: 153200
  gini_index: 0.4417
  vacancy_rate: 12.3
  race_white: 36937
  race_black: 6422
  race_asian: 508
  race_native: 11544
  hispanic: 4961
  bachelors_plus: 10963
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ok/districts/senate/8"
    rel: in-district
    area_weight: 0.5129
  - to: "us/states/ok/districts/senate/9"
    rel: in-district
    area_weight: 0.487
  - to: "us/states/ok/districts/house/13"
    rel: in-district
    area_weight: 0.4305
  - to: "us/states/ok/districts/house/15"
    rel: in-district
    area_weight: 0.3851
  - to: "us/states/ok/districts/house/14"
    rel: in-district
    area_weight: 0.1201
  - to: "us/states/ok/districts/house/16"
    rel: in-district
    area_weight: 0.0642
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Muskogee County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66444 |
| Under 18 | 16195 |
| 18–64 | 38803 |
| 65+ | 11446 |
| Median household income | 53619 |
| Poverty rate | 19.12 |
| Homeownership rate | 66.52 |
| Unemployment rate | 5.66 |
| Median home value | 153200 |
| Gini index | 0.4417 |
| Vacancy rate | 12.3 |
| White | 36937 |
| Black | 6422 |
| Asian | 508 |
| Native | 11544 |
| Hispanic/Latino | 4961 |
| Bachelor's or higher | 10963 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 8](/us/states/ok/districts/senate/8.md) — 51% (state senate)
- [OK Senate District 9](/us/states/ok/districts/senate/9.md) — 49% (state senate)
- [OK House District 13](/us/states/ok/districts/house/13.md) — 43% (state house)
- [OK House District 15](/us/states/ok/districts/house/15.md) — 39% (state house)
- [OK House District 14](/us/states/ok/districts/house/14.md) — 12% (state house)
- [OK House District 16](/us/states/ok/districts/house/16.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
