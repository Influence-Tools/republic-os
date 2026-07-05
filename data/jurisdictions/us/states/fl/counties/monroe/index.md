---
type: Jurisdiction
title: "Monroe County, FL"
classification: county
fips: "12087"
state: "FL"
demographics:
  population: 81860
  population_under_18: 12831
  population_18_64: 48782
  population_65_plus: 20247
  median_household_income: 87738
  poverty_rate: 10.65
  homeownership_rate: 65.79
  unemployment_rate: 2.93
  median_home_value: 780600
  gini_index: 0.5168
  vacancy_rate: 37.26
  race_white: 57200
  race_black: 6012
  race_asian: 929
  race_native: 96
  hispanic: 20132
  bachelors_plus: 34821
districts:
  - to: "us/states/fl/districts/28"
    rel: in-district
    area_weight: 0.2823
  - to: "us/states/fl/districts/senate/40"
    rel: in-district
    area_weight: 0.2587
  - to: "us/states/fl/districts/house/120"
    rel: in-district
    area_weight: 0.2587
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Monroe County, FL

County jurisdiction — 40 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 81860 |
| Under 18 | 12831 |
| 18–64 | 48782 |
| 65+ | 20247 |
| Median household income | 87738 |
| Poverty rate | 10.65 |
| Homeownership rate | 65.79 |
| Unemployment rate | 2.93 |
| Median home value | 780600 |
| Gini index | 0.5168 |
| Vacancy rate | 37.26 |
| White | 57200 |
| Black | 6012 |
| Asian | 929 |
| Native | 96 |
| Hispanic/Latino | 20132 |
| Bachelor's or higher | 34821 |

## Districts

- [FL-28](/us/states/fl/districts/28.md) — 28% (congressional)
- [FL Senate District 40](/us/states/fl/districts/senate/40.md) — 26% (state senate)
- [FL House District 120](/us/states/fl/districts/house/120.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
