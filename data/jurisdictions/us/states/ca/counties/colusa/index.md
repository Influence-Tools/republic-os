---
type: Jurisdiction
title: "Colusa County, CA"
classification: county
fips: "06011"
state: "CA"
demographics:
  population: 21984
  population_under_18: 5914
  population_18_64: 12660
  population_65_plus: 3410
  median_household_income: 75672
  poverty_rate: 11.39
  homeownership_rate: 62.22
  unemployment_rate: 9.78
  median_home_value: 393400
  gini_index: 0.4667
  vacancy_rate: 8.51
  race_white: 8466
  race_black: 335
  race_asian: 215
  race_native: 316
  hispanic: 13832
  bachelors_plus: 2922
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/4"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Colusa County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21984 |
| Under 18 | 5914 |
| 18–64 | 12660 |
| 65+ | 3410 |
| Median household income | 75672 |
| Poverty rate | 11.39 |
| Homeownership rate | 62.22 |
| Unemployment rate | 9.78 |
| Median home value | 393400 |
| Gini index | 0.4667 |
| Vacancy rate | 8.51 |
| White | 8466 |
| Black | 335 |
| Asian | 215 |
| Native | 316 |
| Hispanic/Latino | 13832 |
| Bachelor's or higher | 2922 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 4](/us/states/ca/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
