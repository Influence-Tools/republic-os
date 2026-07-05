---
type: Jurisdiction
title: "Washakie County, WY"
classification: county
fips: "56043"
state: "WY"
demographics:
  population: 7703
  population_under_18: 1615
  population_18_64: 4218
  population_65_plus: 1870
  median_household_income: 65714
  poverty_rate: 8.82
  homeownership_rate: 74.22
  unemployment_rate: 2.71
  median_home_value: 206000
  gini_index: 0.4241
  vacancy_rate: 11.94
  race_white: 6355
  race_black: 9
  race_asian: 26
  race_native: 33
  hispanic: 1089
  bachelors_plus: 1742
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/house/27"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Washakie County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7703 |
| Under 18 | 1615 |
| 18–64 | 4218 |
| 65+ | 1870 |
| Median household income | 65714 |
| Poverty rate | 8.82 |
| Homeownership rate | 74.22 |
| Unemployment rate | 2.71 |
| Median home value | 206000 |
| Gini index | 0.4241 |
| Vacancy rate | 11.94 |
| White | 6355 |
| Black | 9 |
| Asian | 26 |
| Native | 33 |
| Hispanic/Latino | 1089 |
| Bachelor's or higher | 1742 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 20](/us/states/wy/districts/senate/20.md) — 100% (state senate)
- [WY House District 27](/us/states/wy/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
