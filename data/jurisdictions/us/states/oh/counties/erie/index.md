---
type: Jurisdiction
title: "Erie County, OH"
classification: county
fips: "39043"
state: "OH"
demographics:
  population: 74581
  population_under_18: 14492
  population_18_64: 42406
  population_65_plus: 17683
  median_household_income: 71993
  poverty_rate: 12.97
  homeownership_rate: 71.89
  unemployment_rate: 5.33
  median_home_value: 199700
  gini_index: 0.4516
  vacancy_rate: 15.71
  race_white: 60237
  race_black: 6235
  race_asian: 646
  race_native: 49
  hispanic: 3410
  bachelors_plus: 21054
districts:
  - to: "us/states/oh/districts/09"
    rel: in-district
    area_weight: 0.4545
  - to: "us/states/oh/districts/senate/2"
    rel: in-district
    area_weight: 0.4101
  - to: "us/states/oh/districts/house/89"
    rel: in-district
    area_weight: 0.4101
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Erie County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 74581 |
| Under 18 | 14492 |
| 18–64 | 42406 |
| 65+ | 17683 |
| Median household income | 71993 |
| Poverty rate | 12.97 |
| Homeownership rate | 71.89 |
| Unemployment rate | 5.33 |
| Median home value | 199700 |
| Gini index | 0.4516 |
| Vacancy rate | 15.71 |
| White | 60237 |
| Black | 6235 |
| Asian | 646 |
| Native | 49 |
| Hispanic/Latino | 3410 |
| Bachelor's or higher | 21054 |

## Districts

- [OH-09](/us/states/oh/districts/09.md) — 45% (congressional)
- [OH Senate District 2](/us/states/oh/districts/senate/2.md) — 41% (state senate)
- [OH House District 89](/us/states/oh/districts/house/89.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
