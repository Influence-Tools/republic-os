---
type: Jurisdiction
title: "Hamilton County, FL"
classification: county
fips: "12047"
state: "FL"
demographics:
  population: 13616
  population_under_18: 3088
  population_18_64: 4395
  population_65_plus: 6133
  median_household_income: 50144
  poverty_rate: 20.13
  homeownership_rate: 79.79
  unemployment_rate: 6.71
  median_home_value: 111200
  gini_index: 0.4211
  vacancy_rate: 24.27
  race_white: 7594
  race_black: 4266
  race_asian: 78
  race_native: 216
  hispanic: 1564
  bachelors_plus: 1444
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Hamilton County, FL

County jurisdiction — 32 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13616 |
| Under 18 | 3088 |
| 18–64 | 4395 |
| 65+ | 6133 |
| Median household income | 50144 |
| Poverty rate | 20.13 |
| Homeownership rate | 79.79 |
| Unemployment rate | 6.71 |
| Median home value | 111200 |
| Gini index | 0.4211 |
| Vacancy rate | 24.27 |
| White | 7594 |
| Black | 4266 |
| Asian | 78 |
| Native | 216 |
| Hispanic/Latino | 1564 |
| Bachelor's or higher | 1444 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 100% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
