---
type: Jurisdiction
title: "Franklin County, FL"
classification: county
fips: "12037"
state: "FL"
demographics:
  population: 12553
  population_under_18: 2163
  population_18_64: 3434
  population_65_plus: 6956
  median_household_income: 64105
  poverty_rate: 16.49
  homeownership_rate: 80.89
  unemployment_rate: 8.47
  median_home_value: 273300
  gini_index: 0.4729
  vacancy_rate: 42.2
  race_white: 9961
  race_black: 1340
  race_asian: 8
  race_native: 8
  hispanic: 707
  bachelors_plus: 4007
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.4345
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.3991
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.3991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Franklin County, FL

County jurisdiction — 26 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12553 |
| Under 18 | 2163 |
| 18–64 | 3434 |
| 65+ | 6956 |
| Median household income | 64105 |
| Poverty rate | 16.49 |
| Homeownership rate | 80.89 |
| Unemployment rate | 8.47 |
| Median home value | 273300 |
| Gini index | 0.4729 |
| Vacancy rate | 42.2 |
| White | 9961 |
| Black | 1340 |
| Asian | 8 |
| Native | 8 |
| Hispanic/Latino | 707 |
| Bachelor's or higher | 4007 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 43% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 40% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
