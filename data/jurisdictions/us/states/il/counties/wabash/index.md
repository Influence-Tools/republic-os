---
type: Jurisdiction
title: "Wabash County, IL"
classification: county
fips: "17185"
state: "IL"
demographics:
  population: 11119
  population_under_18: 2331
  population_18_64: 6279
  population_65_plus: 2509
  median_household_income: 57086
  poverty_rate: 16.69
  homeownership_rate: 76.33
  unemployment_rate: 4.37
  median_home_value: 104900
  gini_index: 0.4987
  vacancy_rate: 12.38
  race_white: 10416
  race_black: 69
  race_asian: 181
  race_native: 6
  hispanic: 239
  bachelors_plus: 1931
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.0051
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.9986
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Wabash County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11119 |
| Under 18 | 2331 |
| 18–64 | 6279 |
| 65+ | 2509 |
| Median household income | 57086 |
| Poverty rate | 16.69 |
| Homeownership rate | 76.33 |
| Unemployment rate | 4.37 |
| Median home value | 104900 |
| Gini index | 0.4987 |
| Vacancy rate | 12.38 |
| White | 10416 |
| Black | 69 |
| Asian | 181 |
| Native | 6 |
| Hispanic/Latino | 239 |
| Bachelor's or higher | 1931 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 99% (congressional)
- [IN-08](/us/states/in/districts/08.md) — 1% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
