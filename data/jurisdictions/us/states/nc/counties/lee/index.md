---
type: Jurisdiction
title: "Lee County, NC"
classification: county
fips: "37105"
state: "NC"
demographics:
  population: 65816
  population_under_18: 15587
  population_18_64: 38946
  population_65_plus: 11283
  median_household_income: 65387
  poverty_rate: 16.47
  homeownership_rate: 67.32
  unemployment_rate: 3.84
  median_home_value: 240200
  gini_index: 0.4214
  vacancy_rate: 7.44
  race_white: 41846
  race_black: 11685
  race_asian: 579
  race_native: 155
  hispanic: 14286
  bachelors_plus: 12750
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9918
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.0082
  - to: "us/states/nc/districts/senate/12"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/51"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Lee County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65816 |
| Under 18 | 15587 |
| 18–64 | 38946 |
| 65+ | 11283 |
| Median household income | 65387 |
| Poverty rate | 16.47 |
| Homeownership rate | 67.32 |
| Unemployment rate | 3.84 |
| Median home value | 240200 |
| Gini index | 0.4214 |
| Vacancy rate | 7.44 |
| White | 41846 |
| Black | 11685 |
| Asian | 579 |
| Native | 155 |
| Hispanic/Latino | 14286 |
| Bachelor's or higher | 12750 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 99% (congressional)
- [NC-09](/us/states/nc/districts/09.md) — 1% (congressional)
- [NC Senate District 12](/us/states/nc/districts/senate/12.md) — 100% (state senate)
- [NC House District 51](/us/states/nc/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
