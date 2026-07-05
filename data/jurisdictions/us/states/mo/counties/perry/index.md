---
type: Jurisdiction
title: "Perry County, MO"
classification: county
fips: "29157"
state: "MO"
demographics:
  population: 18976
  population_under_18: 4275
  population_18_64: 10970
  population_65_plus: 3731
  median_household_income: 62981
  poverty_rate: 13.85
  homeownership_rate: 76.52
  unemployment_rate: 4.91
  median_home_value: 188200
  gini_index: 0.4551
  vacancy_rate: 12.01
  race_white: 17862
  race_black: 131
  race_asian: 156
  race_native: 13
  hispanic: 467
  bachelors_plus: 3569
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/145"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Perry County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18976 |
| Under 18 | 4275 |
| 18–64 | 10970 |
| 65+ | 3731 |
| Median household income | 62981 |
| Poverty rate | 13.85 |
| Homeownership rate | 76.52 |
| Unemployment rate | 4.91 |
| Median home value | 188200 |
| Gini index | 0.4551 |
| Vacancy rate | 12.01 |
| White | 17862 |
| Black | 131 |
| Asian | 156 |
| Native | 13 |
| Hispanic/Latino | 467 |
| Bachelor's or higher | 3569 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 145](/us/states/mo/districts/house/145.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
