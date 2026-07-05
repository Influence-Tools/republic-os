---
type: Jurisdiction
title: "Platte County, WY"
classification: county
fips: "56031"
state: "WY"
demographics:
  population: 8612
  population_under_18: 1742
  population_18_64: 4537
  population_65_plus: 2333
  median_household_income: 67718
  poverty_rate: 7.74
  homeownership_rate: 76.07
  unemployment_rate: 4.58
  median_home_value: 297900
  gini_index: 0.4277
  vacancy_rate: 17.92
  race_white: 7490
  race_black: 29
  race_asian: 0
  race_native: 35
  hispanic: 761
  bachelors_plus: 1850
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wy/districts/house/4"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Platte County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8612 |
| Under 18 | 1742 |
| 18–64 | 4537 |
| 65+ | 2333 |
| Median household income | 67718 |
| Poverty rate | 7.74 |
| Homeownership rate | 76.07 |
| Unemployment rate | 4.58 |
| Median home value | 297900 |
| Gini index | 0.4277 |
| Vacancy rate | 17.92 |
| White | 7490 |
| Black | 29 |
| Asian | 0 |
| Native | 35 |
| Hispanic/Latino | 761 |
| Bachelor's or higher | 1850 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 6](/us/states/wy/districts/senate/6.md) — 100% (state senate)
- [WY House District 4](/us/states/wy/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
