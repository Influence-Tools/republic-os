---
type: Jurisdiction
title: "Collier County, FL"
classification: county
fips: "12021"
state: "FL"
demographics:
  population: 398291
  population_under_18: 72062
  population_18_64: 92872
  population_65_plus: 233357
  median_household_income: 90045
  poverty_rate: 10.69
  homeownership_rate: 76.6
  unemployment_rate: 3.92
  median_home_value: 540700
  gini_index: 0.534
  vacancy_rate: 30.71
  race_white: 259290
  race_black: 26111
  race_asian: 6132
  race_native: 6207
  hispanic: 112189
  bachelors_plus: 175985
districts:
  - to: "us/states/fl/districts/26"
    rel: in-district
    area_weight: 0.7237
  - to: "us/states/fl/districts/19"
    rel: in-district
    area_weight: 0.0555
  - to: "us/states/fl/districts/18"
    rel: in-district
    area_weight: 0.0285
  - to: "us/states/fl/districts/senate/28"
    rel: in-district
    area_weight: 0.8073
  - to: "us/states/fl/districts/house/82"
    rel: in-district
    area_weight: 0.7274
  - to: "us/states/fl/districts/house/81"
    rel: in-district
    area_weight: 0.0668
  - to: "us/states/fl/districts/house/80"
    rel: in-district
    area_weight: 0.0131
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Collier County, FL

County jurisdiction — 43 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 398291 |
| Under 18 | 72062 |
| 18–64 | 92872 |
| 65+ | 233357 |
| Median household income | 90045 |
| Poverty rate | 10.69 |
| Homeownership rate | 76.6 |
| Unemployment rate | 3.92 |
| Median home value | 540700 |
| Gini index | 0.534 |
| Vacancy rate | 30.71 |
| White | 259290 |
| Black | 26111 |
| Asian | 6132 |
| Native | 6207 |
| Hispanic/Latino | 112189 |
| Bachelor's or higher | 175985 |

## Districts

- [FL-26](/us/states/fl/districts/26.md) — 72% (congressional)
- [FL-19](/us/states/fl/districts/19.md) — 6% (congressional)
- [FL-18](/us/states/fl/districts/18.md) — 3% (congressional)
- [FL Senate District 28](/us/states/fl/districts/senate/28.md) — 81% (state senate)
- [FL House District 82](/us/states/fl/districts/house/82.md) — 73% (state house)
- [FL House District 81](/us/states/fl/districts/house/81.md) — 7% (state house)
- [FL House District 80](/us/states/fl/districts/house/80.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
