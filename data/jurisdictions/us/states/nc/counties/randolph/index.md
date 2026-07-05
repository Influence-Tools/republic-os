---
type: Jurisdiction
title: "Randolph County, NC"
classification: county
fips: "37151"
state: "NC"
demographics:
  population: 146348
  population_under_18: 32538
  population_18_64: 86922
  population_65_plus: 26888
  median_household_income: 61022
  poverty_rate: 14.5
  homeownership_rate: 72.54
  unemployment_rate: 3.48
  median_home_value: 197100
  gini_index: 0.4191
  vacancy_rate: 8.24
  race_white: 114219
  race_black: 9125
  race_asian: 1935
  race_native: 508
  hispanic: 20523
  bachelors_plus: 23346
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/senate/29"
    rel: in-district
    area_weight: 0.7693
  - to: "us/states/nc/districts/senate/25"
    rel: in-district
    area_weight: 0.2306
  - to: "us/states/nc/districts/house/78"
    rel: in-district
    area_weight: 0.6281
  - to: "us/states/nc/districts/house/70"
    rel: in-district
    area_weight: 0.303
  - to: "us/states/nc/districts/house/54"
    rel: in-district
    area_weight: 0.0688
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Randolph County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 146348 |
| Under 18 | 32538 |
| 18–64 | 86922 |
| 65+ | 26888 |
| Median household income | 61022 |
| Poverty rate | 14.5 |
| Homeownership rate | 72.54 |
| Unemployment rate | 3.48 |
| Median home value | 197100 |
| Gini index | 0.4191 |
| Vacancy rate | 8.24 |
| White | 114219 |
| Black | 9125 |
| Asian | 1935 |
| Native | 508 |
| Hispanic/Latino | 20523 |
| Bachelor's or higher | 23346 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 100% (congressional)
- [NC Senate District 29](/us/states/nc/districts/senate/29.md) — 77% (state senate)
- [NC Senate District 25](/us/states/nc/districts/senate/25.md) — 23% (state senate)
- [NC House District 78](/us/states/nc/districts/house/78.md) — 63% (state house)
- [NC House District 70](/us/states/nc/districts/house/70.md) — 30% (state house)
- [NC House District 54](/us/states/nc/districts/house/54.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
