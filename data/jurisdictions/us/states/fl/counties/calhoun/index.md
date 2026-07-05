---
type: Jurisdiction
title: "Calhoun County, FL"
classification: county
fips: "12013"
state: "FL"
demographics:
  population: 13492
  population_under_18: 2964
  population_18_64: 4248
  population_65_plus: 6280
  median_household_income: 50517
  poverty_rate: 20.75
  homeownership_rate: 78.77
  unemployment_rate: 8.01
  median_home_value: 145300
  gini_index: 0.4628
  vacancy_rate: 18.42
  race_white: 10296
  race_black: 1560
  race_asian: 103
  race_native: 115
  hispanic: 709
  bachelors_plus: 1770
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/fl/districts/house/5"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Calhoun County, FL

County jurisdiction — 27 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13492 |
| Under 18 | 2964 |
| 18–64 | 4248 |
| 65+ | 6280 |
| Median household income | 50517 |
| Poverty rate | 20.75 |
| Homeownership rate | 78.77 |
| Unemployment rate | 8.01 |
| Median home value | 145300 |
| Gini index | 0.4628 |
| Vacancy rate | 18.42 |
| White | 10296 |
| Black | 1560 |
| Asian | 103 |
| Native | 115 |
| Hispanic/Latino | 709 |
| Bachelor's or higher | 1770 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 100% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 100% (state senate)
- [FL House District 5](/us/states/fl/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
