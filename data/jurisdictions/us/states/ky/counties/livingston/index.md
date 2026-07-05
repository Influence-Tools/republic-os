---
type: Jurisdiction
title: "Livingston County, KY"
classification: county
fips: "21139"
state: "KY"
demographics:
  population: 8903
  population_under_18: 1963
  population_18_64: 4945
  population_65_plus: 1995
  median_household_income: 58984
  poverty_rate: 19.26
  homeownership_rate: 81.18
  unemployment_rate: 4.21
  median_home_value: 125600
  gini_index: 0.4242
  vacancy_rate: 22.35
  race_white: 8404
  race_black: 75
  race_asian: 11
  race_native: 5
  hispanic: 226
  bachelors_plus: 1368
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/senate/2"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/house/3"
    rel: in-district
    area_weight: 0.9986
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Livingston County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8903 |
| Under 18 | 1963 |
| 18–64 | 4945 |
| 65+ | 1995 |
| Median household income | 58984 |
| Poverty rate | 19.26 |
| Homeownership rate | 81.18 |
| Unemployment rate | 4.21 |
| Median home value | 125600 |
| Gini index | 0.4242 |
| Vacancy rate | 22.35 |
| White | 8404 |
| Black | 75 |
| Asian | 11 |
| Native | 5 |
| Hispanic/Latino | 226 |
| Bachelor's or higher | 1368 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 2](/us/states/ky/districts/senate/2.md) — 100% (state senate)
- [KY House District 3](/us/states/ky/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
