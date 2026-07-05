---
type: Jurisdiction
title: "Walton County, FL"
classification: county
fips: "12131"
state: "FL"
demographics:
  population: 82948
  population_under_18: 17350
  population_18_64: 48940
  population_65_plus: 16658
  median_household_income: 81986
  poverty_rate: 12.47
  homeownership_rate: 78.59
  unemployment_rate: 4.85
  median_home_value: 425100
  gini_index: 0.5228
  vacancy_rate: 43.92
  race_white: 69331
  race_black: 3406
  race_asian: 920
  race_native: 1089
  hispanic: 7154
  bachelors_plus: 28816
districts:
  - to: "us/states/fl/districts/01"
    rel: in-district
    area_weight: 0.4849
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.3303
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 0.8148
  - to: "us/states/fl/districts/house/5"
    rel: in-district
    area_weight: 0.8148
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Walton County, FL

County jurisdiction — 33 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82948 |
| Under 18 | 17350 |
| 18–64 | 48940 |
| 65+ | 16658 |
| Median household income | 81986 |
| Poverty rate | 12.47 |
| Homeownership rate | 78.59 |
| Unemployment rate | 4.85 |
| Median home value | 425100 |
| Gini index | 0.5228 |
| Vacancy rate | 43.92 |
| White | 69331 |
| Black | 3406 |
| Asian | 920 |
| Native | 1089 |
| Hispanic/Latino | 7154 |
| Bachelor's or higher | 28816 |

## Districts

- [FL-01](/us/states/fl/districts/01.md) — 48% (congressional)
- [FL-02](/us/states/fl/districts/02.md) — 33% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 81% (state senate)
- [FL House District 5](/us/states/fl/districts/house/5.md) — 81% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
