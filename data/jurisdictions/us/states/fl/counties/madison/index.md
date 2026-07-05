---
type: Jurisdiction
title: "Madison County, FL"
classification: county
fips: "12079"
state: "FL"
demographics:
  population: 18089
  population_under_18: 3196
  population_18_64: 10750
  population_65_plus: 4143
  median_household_income: 48485
  poverty_rate: 21.0
  homeownership_rate: 73.41
  unemployment_rate: 5.81
  median_home_value: 116200
  gini_index: 0.4393
  vacancy_rate: 17.13
  race_white: 10092
  race_black: 6506
  race_asian: 22
  race_native: 40
  hispanic: 1051
  bachelors_plus: 2578
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/9"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Madison County, FL

County jurisdiction — 36 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18089 |
| Under 18 | 3196 |
| 18–64 | 10750 |
| 65+ | 4143 |
| Median household income | 48485 |
| Poverty rate | 21.0 |
| Homeownership rate | 73.41 |
| Unemployment rate | 5.81 |
| Median home value | 116200 |
| Gini index | 0.4393 |
| Vacancy rate | 17.13 |
| White | 10092 |
| Black | 6506 |
| Asian | 22 |
| Native | 40 |
| Hispanic/Latino | 1051 |
| Bachelor's or higher | 2578 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 100% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 100% (state senate)
- [FL House District 9](/us/states/fl/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
