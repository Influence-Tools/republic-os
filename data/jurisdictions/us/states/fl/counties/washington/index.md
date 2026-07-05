---
type: Jurisdiction
title: "Washington County, FL"
classification: county
fips: "12133"
state: "FL"
demographics:
  population: 25529
  population_under_18: 5110
  population_18_64: 15616
  population_65_plus: 4803
  median_household_income: 58210
  poverty_rate: 17.29
  homeownership_rate: 79.95
  unemployment_rate: 3.57
  median_home_value: 171000
  gini_index: 0.438
  vacancy_rate: 15.91
  race_white: 19668
  race_black: 3463
  race_asian: 150
  race_native: 144
  hispanic: 1026
  bachelors_plus: 3012
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/5"
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

# Washington County, FL

County jurisdiction — 44 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25529 |
| Under 18 | 5110 |
| 18–64 | 15616 |
| 65+ | 4803 |
| Median household income | 58210 |
| Poverty rate | 17.29 |
| Homeownership rate | 79.95 |
| Unemployment rate | 3.57 |
| Median home value | 171000 |
| Gini index | 0.438 |
| Vacancy rate | 15.91 |
| White | 19668 |
| Black | 3463 |
| Asian | 150 |
| Native | 144 |
| Hispanic/Latino | 1026 |
| Bachelor's or higher | 3012 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 100% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 100% (state senate)
- [FL House District 5](/us/states/fl/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
