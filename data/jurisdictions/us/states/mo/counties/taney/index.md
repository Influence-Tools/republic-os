---
type: Jurisdiction
title: "Taney County, MO"
classification: county
fips: "29213"
state: "MO"
demographics:
  population: 56529
  population_under_18: 11799
  population_18_64: 31862
  population_65_plus: 12868
  median_household_income: 56497
  poverty_rate: 15.63
  homeownership_rate: 67.03
  unemployment_rate: 3.9
  median_home_value: 218800
  gini_index: 0.4687
  vacancy_rate: 24.48
  race_white: 48837
  race_black: 1065
  race_asian: 569
  race_native: 147
  hispanic: 4307
  bachelors_plus: 13119
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/155"
    rel: in-district
    area_weight: 0.7852
  - to: "us/states/mo/districts/house/156"
    rel: in-district
    area_weight: 0.2146
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Taney County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56529 |
| Under 18 | 11799 |
| 18–64 | 31862 |
| 65+ | 12868 |
| Median household income | 56497 |
| Poverty rate | 15.63 |
| Homeownership rate | 67.03 |
| Unemployment rate | 3.9 |
| Median home value | 218800 |
| Gini index | 0.4687 |
| Vacancy rate | 24.48 |
| White | 48837 |
| Black | 1065 |
| Asian | 569 |
| Native | 147 |
| Hispanic/Latino | 4307 |
| Bachelor's or higher | 13119 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 155](/us/states/mo/districts/house/155.md) — 79% (state house)
- [MO House District 156](/us/states/mo/districts/house/156.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
