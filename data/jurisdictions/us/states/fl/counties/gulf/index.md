---
type: Jurisdiction
title: "Gulf County, FL"
classification: county
fips: "12045"
state: "FL"
demographics:
  population: 15131
  population_under_18: 2502
  population_18_64: 4665
  population_65_plus: 7964
  median_household_income: 61179
  poverty_rate: 12.47
  homeownership_rate: 80.79
  unemployment_rate: 2.63
  median_home_value: 250000
  gini_index: 0.4818
  vacancy_rate: 36.51
  race_white: 11768
  race_black: 2078
  race_asian: 94
  race_native: 100
  hispanic: 737
  bachelors_plus: 3947
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.7304
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.7154
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.7154
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Gulf County, FL

County jurisdiction — 25 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15131 |
| Under 18 | 2502 |
| 18–64 | 4665 |
| 65+ | 7964 |
| Median household income | 61179 |
| Poverty rate | 12.47 |
| Homeownership rate | 80.79 |
| Unemployment rate | 2.63 |
| Median home value | 250000 |
| Gini index | 0.4818 |
| Vacancy rate | 36.51 |
| White | 11768 |
| Black | 2078 |
| Asian | 94 |
| Native | 100 |
| Hispanic/Latino | 737 |
| Bachelor's or higher | 3947 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 73% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 72% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 72% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
