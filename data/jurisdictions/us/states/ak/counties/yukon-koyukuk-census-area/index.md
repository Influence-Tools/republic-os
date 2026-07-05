---
type: Jurisdiction
title: "Yukon-Koyukuk Census Area, AK"
classification: county
fips: "02290"
state: "AK"
demographics:
  population: 5195
  population_under_18: 1393
  population_18_64: 1732
  population_65_plus: 2070
  median_household_income: 55741
  poverty_rate: 16.02
  homeownership_rate: 69.9
  unemployment_rate: 5.39
  median_home_value: 98500
  gini_index: 0.4425
  vacancy_rate: 38.35
  race_white: 1145
  race_black: 100
  race_asian: 72
  race_native: 3419
  hispanic: 115
  bachelors_plus: 780
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ak/districts/senate/r"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ak/districts/house/36"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Yukon-Koyukuk Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5195 |
| Under 18 | 1393 |
| 18–64 | 1732 |
| 65+ | 2070 |
| Median household income | 55741 |
| Poverty rate | 16.02 |
| Homeownership rate | 69.9 |
| Unemployment rate | 5.39 |
| Median home value | 98500 |
| Gini index | 0.4425 |
| Vacancy rate | 38.35 |
| White | 1145 |
| Black | 100 |
| Asian | 72 |
| Native | 3419 |
| Hispanic/Latino | 115 |
| Bachelor's or higher | 780 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 100% (congressional)
- [AK Senate District R](/us/states/ak/districts/senate/r.md) — 100% (state senate)
- [AK House District 36](/us/states/ak/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
